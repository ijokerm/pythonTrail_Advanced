"""
演示面向对象--多继承
注意：对于父类中同名的成员（成员属性和成员方法）访问时，按照左边的先来 谁先继承谁的优先级高
"""
class Phone:
    IMEI = None     # 序列号
    producer = "SP" #厂商
    __store = 512

    def call_by_4g(self):
        print("4g通话")

class NFCReader:
    NFC_type = "第五代"
    producer = "SPbear"

    def read_card(self):
        print("NFC读卡")

    def write_card(self):
        print("NFC写卡")

class RemoteControl:
    RC_type = "红外遥控"

    def control(self):
        print("红外遥控开启了")

class myPhone(Phone,NFCReader,RemoteControl):
    pass  # 作用是不产生语法错误 pass是占位语句，用来保证函数（方法）或类定义的完整性，表示无内容，空的意思

phone = myPhone()
phone.call_by_4g()
phone.read_card()
phone.write_card()
phone.control()
print(phone.producer)

