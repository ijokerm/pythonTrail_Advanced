"""
演示面向对象--继承--单继承基础语法
注意：父类中的私有成员和私有方法是不能被继承的
"""
# 父类
class Phone:
    IMEI = None     # 序列号
    producer = "SP" #厂商
    __store = 512

    def call_by_4g(self):
        print("4g通话")



# 单继承
class Phone2022(Phone):
    faceID = "10001"   #面部识别

    def call_by_5g(self):
        print("2022年新功能：5G通话")

phone = Phone2022()
print(phone.producer)
phone.call_by_4g()
phone.call_by_5g()