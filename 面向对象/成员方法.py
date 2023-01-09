"""
演示面向对象类中的成员方法定义和使用
"""
# 定义一个带有成员方法的类
class Student:
    name = None

    def say_hi(self):
        print(f"大家好，我是{self.name}")

    def say_hi2(self,msg):
        print(f"大家好，我是{self.name},{msg}")
stu_1 = Student()
stu_1.name = "李四"
stu_1.say_hi2("哎哟不错呀")

stu_2 = Student()
stu_2.name = "李wy"
stu_2.say_hi()

