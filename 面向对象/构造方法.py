"""
演示类的构造方法
"""
# 使用构造方法对成员变量进行赋值
# 使用构造方法的名称 __init__

class Student:
    name = None
    age = None
    tel = None

    def __init__(self,name,age,tel):
        self.name = name
        self.age = age
        self.tel = tel
        print("Stuent类创建了一个类对象") # 验证__init__是否可以自动执行

stu = Student("周姐",31,"177889988776")
print(stu.name)
print(stu.age)
print(stu)

