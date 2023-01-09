"""
演示Union联合注解
注意 使用Union类型必须先导包
"""
from typing import Union
my_list: list[Union[int,str]] = [1,3,"sdf","er"]

def func(data: Union[int,str])-> Union[int,str]:
    pass
func()