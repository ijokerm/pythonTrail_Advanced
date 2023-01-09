"""
演示面向对象封装思想中私有成员的使用
"""
class Phone:
    __cunrent_voltage = 0.3  # 当前手机运行电压 私有

    def __keep_single_core(self):  # 私有方法
        print("让CPU以单核模式运行")

    def call_by_5g(self):
        if self.__cunrent_voltage >= 1:
            print("5g通话已开启")
        else:
            self.__keep_single_core()
            print("电量不足，无法使用5G通话，并已设置为单核模式。")

phone = Phone()
phone.call_by_5g()