# -*- coding:utf-8 -*-
# @Time:2021/5/18 16:54
# @Author:ui_none


import re
import time
import com
import data_process


if __name__ == "__main__":
    start_time = time.perf_counter()
    # content = "信息抽取之 DFA 算法匹配关键词，匹配算法，信息抓取"
    content = com.load_content()
    content_list = list(content)
    # keyword_list = ["信息抽取", "匹配", "匹配关键词", "匹配算法"]
    keyword_list = com.read_multiple_lines_from_txt('.\\input\\keywords.txt')

    state_dict = data_process.generate_state_event_dict(keyword_list)  # 获取关键字列表并生成hash_map
    res_match_list = data_process.match(state_dict, content)  # 根据hash_map和content生成匹配列表
    after_process_content = data_process.process_content(content, res_match_list, '-')  # 根据匹配列表和文本生成处理后的结果并返回

    end_time = time.perf_counter()
    print('-'*50)
    print(f'耗时{end_time-start_time}秒')
    print(f'原文本:{content}')
    print(f'处理后文本:{after_process_content}')
    print(f'keywords_list:{keyword_list}')
    print(f'match_list:{res_match_list}')
    print(f'state_dict:{state_dict}')
