# API使用手册
## 数据处理
数据处理任务放在data_process.py中，有着相应的api接口。下面简单介绍api及相应的功能。
- generate_state_event_dict
- match
- process_content

generate_state_event_dict()接收一个关键字的list，并根据这个keyword list生成字典树，便于进行匹配

match()接收字典树和文本作为参数，并返回匹配位置和匹配文本的字典列表

process_content()接收文本、match()返回的匹配字典列表和指定掩码作为参数，可根据关键词匹配字典对接收的文本进行屏蔽处理，可指定屏蔽文字。

## 文本操作
文本（json、pickle、txt）等的读写操作放在com.py中，同样简单介绍api接口及相应的功能。
- read_single_line_from_txt
- read_multiple_lines_from_txt
- load_content
- save_dfa_object
- load_dfa_object
- save_hash_map

read_single_line_from_txt()接收一个文本路径，将指定路径的文本内容进行**单行**读取并返回生成的关键词列表。

read_multiple_lines_from_txt()同样接收一个文本路径，将指定路径的文本内容进行**多行**读取并返回生成的关键词列表。

>P.S.:读取的txt文件的内容需要以英文输入状态下的','进行分隔。

load_content()接收一个文件路径作为参数，将文本的内容读出并返回一个str。

save_dfa_object()和load_dfa_object()是对创建的DFA类对象进行保存、读取的方法，save_dfa_object()接收一个dfa对象和文件路径作为参数，而load_dfa_object()接收一个文件路径作为参数，读取出dfa对象。

save_hash_map()则接收一个文件路径作为参数，将data_process文件中match()方法生成的字典列表保存到指定路径的文件中。

>P.S.:以上关于文件路径的参数都已设定了默认参数，推荐使用默认参数指定的位置进行保存。当然自己指定保存/读取路径也行。
