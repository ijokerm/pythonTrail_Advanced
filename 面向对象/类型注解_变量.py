"""
演示变量的类型注解：
"""
import json
import random

# 基础数据类型注解
var1: int = 12
var2: str = "test"
var3: bool = True
# 类对象类型注解
class Student:
    pass
stu: Student =Student()
# 基础容器类型注解
my_list: list = [1,2,'a']
my_tuple: tuple = (2,3,3,4)
my_dict: dict = {"key":221}
# 容器类型详细注解
my_list: list[int] = [1,2,3]
my_tuple: tuple[int] = (2,3,3,4)
my_dict: dict[str:int] = {"key":221}
# 在注释中进行类型注解 快捷键：alt+enter 可以搜索自动导包
var_1 = random.randint(1,10)  # type: int
var_2 = json.loads('{"name":"张三"}') # type: dict[str:str]
def func():
    return 10
var_3 = func() # type: int
# 类型注解的限制