# This file prepocess level data.

# Input from folder Original
# Output to folder OneLine
# Run this file in folder Bunstack!

import os

objlist = ["f", "b", "c", "n"]

def add_space_after_slash(s, rlist):
    """
    在字符串s中，找到第一个"/"字符后面的所有"b"字符，并将它们替换为"b "。
    """
    # 查找第一个"/"的位置
    slash_index = s.find('/')
    # print(f"slash_index: {slash_index}")
    # 如果找到了"/"
    if slash_index != -1:
        # 将字符串分为两部分："/"之前的部分和"/"之后的部分
        before_slash = s[:slash_index + 1]
        after_slash = s[slash_index + 1:]
        
        # 只对"/"之后的部分进行替换操作
        for t in rlist:
            after_slash = after_slash.replace(str(t), str(t)+' ')
        
        # 将处理后的两部分拼接起来
        result = before_slash + after_slash
    else:
        # 如果没有找到"/"，则不做任何替换
        result = s
    
    return result

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

        modified_content = add_space_after_slash(modified_content, objlist)
        
        # 写入修改后的内容到新文件
        with open(output_file_path, 'w', encoding='utf-8') as file:
            file.write(modified_content)
        
        print("文件处理完成。")
    except FileNotFoundError:
        # 如果抛出了 FileNotFoundError 异常，则执行这里的代码
        # print(f"文件{input_file_path}不存在，跳过不处理。")
        pass
    except Exception as e:
        print(f"处理文件时发生错误: {e}")

print("当前工作目录:", os.getcwd())

for LevelPack in ["W", "N", "C", "S", "E", "NW", "NE", "SW", "SE"]:
    for i in range(1, 28):
        input_file_path = os.path.join('.', 'LevelData','Original', LevelPack, LevelPack + str(i) + '.txt')  # 输入文件路径
        output_file_path = os.path.join('.','LevelData','OneLine', LevelPack, LevelPack + str(i) + '.txt')  # 输出文件路径
        # 调用函数
        replace_first_newline(input_file_path, output_file_path)

#todo: 检查兔子数量是否正确, warning 缺少出入口的关卡, 检查上下层o&f关系
