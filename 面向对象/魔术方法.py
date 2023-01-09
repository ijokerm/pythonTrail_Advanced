"""
演示Python内置的各类魔术方法
"""
class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    # __str__ 控制类对象转变为字符串
    def __str__(self):
        return f"{self.name},{self.age}"

    # __lt__ 小于符号比较方法--实现小于符号 和 大于符号 2种比较
    def __lt__(self, other):
        return self.age < other.age

    # __le__ 小于等于比较符号方法--实现<=、>=两种比较运算符
    def __le__(self, other):
        return self.age <= other.age
    # __eq__ 比较运算符实现方法
    def __eq__(self, other):
        return self.age == other.age

stu1 = Student("自制力",32)
stu2 = Student("养成",21)
print(stu1)      # 输出：自制力,32
print(str(stu1)) # 输出：自制力,32
print(stu1.age > stu2.age)
print(stu1.age < stu2.age)
print(stu1.age <= stu2.age)
print(stu1.age >= stu2.age)
print(stu1.age == stu2.age)







