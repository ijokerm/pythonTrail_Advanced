"""
演示Python正则表达式re模块的3个基础匹配方法
"""
import re
s = "1pythonrning21bearupupythonread"

# match 从头匹配
result = re.match("21",s)
# print(result)
# print(result.span())
# print(result.group())

# search 搜索匹配
result1 = re.search("python",s)
print(result1)
print(result1.span(),result1.group())

# findall 搜索全部匹配
result2 = re.findall("python",s)
print(result2)
