import os
import json


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
