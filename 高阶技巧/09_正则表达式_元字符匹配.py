"""
演示Python正则表达式使用元字符进行匹配
"""
import re

# s = "ityuii@@python 22#d456opi\duhj2"
# result = re.findall('[0-9]',s)    # 字符串前面加上r标记表示字符串中的转义字符无效在，就是普通字符的意思
# print(result)

# 匹配账号，只能由字母和数字组成，长度限制6到10位
# r = '^[0-9a-zA-Z]{6,10}$'
# s = "1234567A_"
# print(re.findall(r,s))
# 匹配QQ号，要求纯数字，长度5-11，第一位不为0
# r = '^[1-9][0-9]{4,10}$'
# s = "24113A9"
# print(re.findall(r,s))
# 匹配邮箱地址，只能允许qq、163、gmail这三种邮箱的地址
# {内容}.{内容}.{内容}@{qq、163、gmail}.{}.{}..
r = r'(^[\w]+(\.[\w])*@(qq|163|gmail)(\.[\w]+)*$)'
s = "200aa9998@qq.com"
print(re.match(r,s))