"""
面向对象继承--复写使用父类成员
"""
# 父类
class Phone:
    IMEI = "20221210"
    producer = "SP"

    def call_by_5g(self):
        print("5g通话模式")

# 定义子类 复写父类
class myPhone(Phone):
    producer = "SPplus"

    def call_by_5g(self):
        print("开启CPU单核模式，保持通话省电")
        # # 方式1 通过父类名调用父类里面的成员
        # print(f"父类的厂商：{Phone.producer}")
        # Phone.call_by_5g(self)    # 调用父类的成员方法 括号内一定要加self
        # 方式2 利用super
        print(f"父类的厂商：{super().producer}")
        super().call_by_5g()
        print("关闭CPU单核模式，确保性能")

phone = myPhone()
phone.call_by_5g()
print(phone.producer,phone.IMEI)