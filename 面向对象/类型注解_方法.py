"""
演示方法的类型注解 形参+返回值
"""
def func1(data:list):
    return data
print(func1([2,2,3]))

def func2(value) -> set:
    return value
print(func2(23))
