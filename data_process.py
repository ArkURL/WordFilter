# -*- coding:utf-8 -*-
# @Time:2021/5/19 23:09
# @Author:ui_none

import copy


# 返回关键字字典HashMap
def generate_state_event_dict(keyword_list: list) -> dict:
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


# 输入关键字和文本内容，返回匹配列表
def match(state_event_dict: dict, content: str):
    match_list = []
    state_list = []
    temp_match_list = []

    for char_pos, char in enumerate(content):
        if char in state_event_dict:
            state_list.append(state_event_dict)
            temp_match_list.append({
                "start": char_pos,
                "match": "",
                "length": 0
            })

        for index, state in enumerate(state_list):
            if char in state:
                state_list[index] = state[char]
                temp_match_list[index]["match"] += char
                temp_match_list[index]["length"] += 1

                if state[char]["is_end"]:
                    match_list.append(copy.deepcopy(temp_match_list[index]))

                    if len(state[char].keys()) == 1:
                        state_list.pop(index)
                        temp_match_list.pop(index)
            else:
                state_list.pop(index)
                temp_match_list.pop(index)

    return match_list


# 根据匹配结果列表处理输入文本
def process_content(content: str, res_match_list: list, mask_code: str) -> str:
    content_list = list(content)
    for each in res_match_list:
        length = each['length']
        start = each['start']
        content_list[start:start+length] = mask_code*length
    after_process_content = "".join(content_list)
    return after_process_content
