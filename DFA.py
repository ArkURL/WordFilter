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
                if char in state:  # 如果在字典中查到
                    state_list[index] = state[char]  # 更新，进入字典下一层
                    temp_match_list[index]["match"] += char
                    temp_match_list[index]["length"] += 1

                    if state[char]["is_end"]:   # 如果更新后是字典最后一层，匹配完成
                        match_list.append(copy.deepcopy(temp_match_list[index]))
                        # 提前执行pop操作，减少后面的content匹配所需时间
                        if len(state[char].keys()) == 1:    # 个人感觉这层判断可以不要，因为已经通过了is_end=True的判断了，此时
                            state_list.pop(index)           # len(state[char].keys())返回值一定为1
                            temp_match_list.pop(index)
                else:   # 字典中没有查询到char，将会把state_list中不匹配的字典pop出，同时temp_match_list也将pop出内容
                    state_list.pop(index)   # 若state_list为空，enumerate处理之后pop不会有反应
                    temp_match_list.pop(index)

        return match_list

    @staticmethod
    def _generate_state_event_dict(keyword_list: list) -> dict:
        state_event_dict = {}

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
