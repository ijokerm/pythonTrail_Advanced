"""
设计一个类，记录学生的：
姓名、年龄、地址，这3类信息
通过for循环，配合input输入语句，并使用构造方法，完成学生信息的键盘录入
输入完成后，使用print语句，完成信息的输出
"""
class Student:
    name = None
    age = None
    addres = None

    def __init__(self,name,age,addres):
        self.name = name
        self.age = age
        self.addres = addres


for x in range(1,10):
    name_in = input("请输入学生姓名:")
    age_in = input("请输入学生年龄：")
    address_in = input("请输入学生地址：")
    stu = Student(name_in,age_in,address_in)
    print(f"当前录入第{x}位学生信息，总共需要录入10位学生信息")
    print(f"学生{x}信息录入完成,信息为：【学生姓名：{stu.name},年龄：{stu.age},地址：{stu.addres}】")

print("所有学生的信息录入完毕")
