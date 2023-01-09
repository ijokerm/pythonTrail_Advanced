"""
演示Python递归操作
需求：通过递归找出一个文件夹中全部的文件
思路: 写一个函数，列出文件夹内的全部内容，如果是文件就收集到list
如果是文件夹，就递归调用自己再次判断
"""
import os

# print(os.listdir("E:/test"))      # 列出指定目录下的内容
# print(os.path.isdir("E:/test"))   # 判断给定路径是否是文件夹，是返回True，否返回False
# print(os.path.exists("E:/test"))  # 判断给定路径是否存在，存在返回True，否则返回False

def get_files(path):
    file_list = []
    if os.path.exists(path):
        for p in os.listdir(path):
            new_path = path + '/' + p
            if os.path.isdir(new_path):
                file_list += get_files(new_path)
            else:
                file_list.append(new_path)
    else:
        print(f"指定的目录{path}不存在")
        return []

    return file_list


if __name__ == '__main__':
    print(get_files("E:/test"))
