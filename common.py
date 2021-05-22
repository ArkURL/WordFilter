# -*- coding:utf-8 -*-
# @Time:2021/5/19 19:19
# @Author:ui_none

import pickle as pik
import json


def fun():
    print('test')


# 从txt文件中读取多行数据并转换为列表
def read_multiple_lines_from_txt(path_to_file: str = '.\\keywords.txt') -> list:
    with open(path_to_file, 'r', encoding='utf-8') as f:
        total_list = []
        for each_str in f.readlines():
            each_str = each_str.strip('\n')  # 返回str
            each_list = each_str.split(',')  # 返回处理后的列表
            total_list.extend(each_list)     # 用each_list拓展total_list
        return total_list


# 从txt文件读取单行数据并转换为列表
def read_single_line_from_txt(path_to_file: str = '.\\keywords.txt') -> list:
    with open(path_to_file, 'r', encoding='utf-8') as f:
        s = f.read()
        keyword_list = s.split(',')
        return keyword_list


# 保存制作好的HashMap
def save_hash_map(hash_map_list: list, output_file_path: str = '.\\hashmap.json') -> None:
    with open(output_file_path, 'w', encoding='utf-8') as f:
        f.write(json.dumps(hash_map_list))


# 保存dfa对象
def save_dfa_object(dfa_object, output_file_path: str = '.\\dfa_object.pik') -> None:
    with open(output_file_path, 'wb+') as f:
        pik.dump(dfa_object, f)


# 读取dfa对象
def load_dfa_object(input_file_path: str = '.\\dfa_object.pik'):
    with open(input_file_path, 'rb') as f:
        dfa_object = pik.load(f)
    return dfa_object


# 从外部文件加载content文本
def load_content(path_to_content: str = '.\\content.txt') -> str:
    with open(path_to_content, 'r', encoding='utf-8') as f:
        content = f.read()
        return content
