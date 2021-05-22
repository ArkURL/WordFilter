# -*- coding:utf-8 -*-
# @Time:2021/5/19 21:00
# @Author:ui_none

import copy


class DFA:
    def __init__(self, keyword_list: list):
        self.state_event_dict = self._generate_state_event_dict(keyword_list)

    def match(self, content: str):
        match_list = []
        state_list = []
        temp_match_list = []

        for char_pos, char in enumerate(content):
            if char in self.state_event_dict:
                state_list.append(self.state_event_dict)
                temp_match_list.append({
                    "start": char_pos,
                    "match": "",
                    "length": 0
                })

            for index, state in enumerate(state_list):
                is_find = False
                state_char = None

                # 遇到通配符"*"，直接更新
                if "*" in state:
                    state_list[index] = state["*"]      # 更新，进入字典下一层
                    state_char = "*"
                    is_find = True

                # 遇到通配符就不用再查了
                elif char in state:  # 如果在字典中查到当前字符
                    state_list[index] = state[char]     # 更新，进入字典下一层
                    state_char = char
                    is_find = True

                if is_find:
                    temp_match_list[index]["match"] += char
                    temp_match_list[index]["length"] += 1

                    if state[state_char]["is_end"]:   # 如果更新后是字典最后一层，匹配完成（若存在包含关系，则最短关键字首先匹配成功）
                        match_list.append(copy.deepcopy(temp_match_list[index]))
                        # 提前执行pop操作，减少后面的content匹配所需时间
                        if len(state[char].keys()) == 1:    # keywords_list中的关键词可能存在包含关系，比如‘自动’与‘自动机’
                            state_list.pop(index)           # 为了避免碰到‘自动’就结束匹配，需要多加一层判断
                            temp_match_list.pop(index)      # 存在包含关系的关键字最终会根据较长的关键字生成hash_map
                    # 相应的，如果state[char]["is_end"]==False,则将等待下一个char的匹配
                    # 若存在关键字交叉在content中出现，意味着先出现的关键字匹配失败，在这个enumerate(state_list)循环中将进入else语句并被pop出
                else:   # 字典中没有查询到char，将会把state_list中不匹配的字典pop出，同时temp_match_list也将pop出内容
                    state_list.pop(index)   # 若state_list为空，enumerate处理之后pop不会有反应
                    temp_match_list.pop(index)

        return match_list

    @staticmethod
    def _generate_state_event_dict(keyword_list: list) -> dict:
        state_event_dict = {}
        # 如果存在一个关键词包含另一个关键词的情况，将返回一个以最长关键词为标准的字典，且较短关键词处的is_end为True
        for keyword in keyword_list:
            current_dict = state_event_dict
            length = len(keyword)

            for index, char in enumerate(keyword):
                if char not in current_dict:
                    next_dict = {"is_end": False}
                    current_dict[char] = next_dict
                    current_dict = next_dict
                else:
                    next_dict = current_dict[char]
                    current_dict = next_dict

                if index == length - 1:
                    current_dict["is_end"] = True

        return state_event_dict
