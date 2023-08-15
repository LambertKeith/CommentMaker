import os
import json
import random
import re
from .langchain_chat import base_chat


#提示词：请你编写一个python函数，读取指定目录的json文件并以列表形式return所有的键
#读取案例json并以列表形式输出
def read_json_keys(directory='data', filename='example.json'):
    # 构建JSON文件的完整路径
    file_path = os.path.join(directory, filename)

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            if isinstance(data, dict):
                return list(data.keys())
            else:
                return []
    except FileNotFoundError:
        print(f"File '{filename}' not found in directory '{directory}'.")
        return []
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON in file '{filename}': {e}")
        return []


#根据描述生成评价
def make_comment(describe, wordCount=150):
    prompt = f"请你扮演小学老师根据下面的描述生成一段对该学生想说的话，不要有另起一行的称呼和结尾，也不要分段,{wordCount}字：" + describe
    print(prompt)
    return base_chat(prompt)
    #base_chat


#提示词：请你编写一个python函数，读取路径为data\example.json的json文件，根据键返回指定值
#读取描述json
def get_value_from_json_file(key, json_file_path="data/example.json"):
    with open(json_file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    return data.get(key, None)


#提示词：请你编写一个python函数，根据传入的键和值在路径为data\example.json的json文件中增加一条
#增加示例
def add_data_to_json_file(key, value, json_file_path="data/example.json"):
    # 读取现有的 JSON 数据
    with open(json_file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    # 添加新的键值对
    data[key] = value

    # 将更新后的数据写回文件
    with open(json_file_path, 'w') as file:
        json.dump(data, file, indent=4)


#
#删除示例
def remove_data_from_json_file(key_to_remove, json_file_path="data/example.json"):
    # 读取现有的 JSON 数据
    with open(json_file_path, 'r') as file:
        data = json.load(file)

    # 删除指定键对应的条目
    if key_to_remove in data:
        del data[key_to_remove]

    # 将更新后的数据写回文件
    with open(json_file_path, 'w') as file:
        json.dump(data, file, indent=4)


#检查名字输入格式
def is_valid_student_name(name):
    # 使用正则表达式检查学生姓名格式
    # 姓名只能包含中文字符
    pattern = r'^[\u4e00-\u9fa5]+$'
    return re.match(pattern, name)

import traceback
#---获取得分对应的描述---

def choose_discribe_from_json(key):
    #读取指定键的值
    def read_score_to_discribe_value(key, json_file_path='data/score_to_discribe.json'):
        print(key)
        try:
            with open(json_file_path, "r", encoding='utf-8') as json_file:
                data = json.load(json_file)
                if key in data:
                    return data[key]
                else:
                    #键不存在
                    return []
        except Exception as e:
            traceback.print_exc(e)
            return False
        
    #从列表中随机选选择几个项目
    def select_random_values(input_list, num_values=4):
        if input_list:
            if num_values < len(input_list):
                random_values = random.sample(input_list, num_values)
                return random_values
    
    disc_list = []
    str_disc = '\n'
    disc_list = read_score_to_discribe_value(key)

    if disc_list != []:
        select_list = select_random_values(disc_list)
        for i in select_list:
            i += ' '
            str_disc += i
        return str_disc



