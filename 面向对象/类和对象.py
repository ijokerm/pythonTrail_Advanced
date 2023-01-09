"""
演示类和对象的关系，即面向对象编程套路（思想）
"""
# 设计一个闹钟类
class Clock:
    id = None
    price = None

    def ring(self):
        import winsound
        winsound.Beep(2000,3000)
# 构键2个闹钟对象并让其工作
clock_1 = Clock()
clock_1.id = "00001"
clock_1.price = 19.99
print(f"闹钟ID：{clock_1.id},价格：{clock_1.price}")
clock_1.ring()

clock_2 = Clock()
clock_2.id = "00002"
clock_2.price = 21.99
print(f"闹钟ID：{clock_1.id},价格：{clock_1.price}")
clock_1.ring()