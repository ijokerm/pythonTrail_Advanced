"""
设计一个手机类，内部包含：
私有成员变量：__is_5g_enable，类型bool，True表示开启5g，False表示关闭5g
私有成员方法：__check_5g()，会判断私有成员__is_5g_enable的值
若为True，打印输出：5g开启
若为False，打印输出：5g关闭，使用4g网络
公开成员方法：call_by_5g()，调用它会执行
调用私有成员方法：__check_5g()，判断5g网络状态
打印输出：正在通话中
"""
class Phone:
    __is_5g_enable = False

    def __check_5g(self):
        if self.__is_5g_enable == True:
            print("5g开启")
        else:
            print("5g关闭，使用4g网络")

    def call_by_5g(self):
        self.__check_5g()
        print("正在通话中")

phone = Phone()
phone.call_by_5g()