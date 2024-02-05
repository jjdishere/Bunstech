# This file prepocess level data.

# Input from folder Original
# Output to folder OneLine
# Run this file in folder Bunstack!

import os

def replace_first_newline(input_file_path, output_file_path):
    """
    读入一个文本文件，把第一个换行符变成字符“/”，剩余换行符替换成空格，然后输出到另一个文本文件。

    :param input_file_path: 输入文件的路径
    :param output_file_path: 输出文件的路径
    """
    try:
        # 读取原始文件内容
        with open(input_file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # 找到第一个换行符并替换为“/”
        content = content.replace('\n', '/', 1)
        
        # 替换剩余的换行符为空格
        modified_content = content.replace('\n', ' ')
        
        # 写入修改后的内容到新文件
        with open(output_file_path, 'w', encoding='utf-8') as file:
            file.write(modified_content)
        
        print("文件处理完成。")
    except Exception as e:
        print(f"处理文件时发生错误: {e}")

print("当前工作目录:", os.getcwd())
# 示例用法
input_file_path = os.path.join('.', 'LevelData','Original', 'W', 'W3.txt')  # 输入文件路径，请根据实际情况替换
output_file_path = os.path.join('.','LevelData','OneLine', 'W', 'W3.txt')  # 输出文件路径，请根据实际情况替换

# 调用函数
replace_first_newline(input_file_path, output_file_path)
