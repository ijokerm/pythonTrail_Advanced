"""
定义文本/json中的数据 定义Record类
"""
class Record:
    # 利用构造方法定义成员变量
    def __init__(self,order_date,order_id,money,province):
        self.order_date = order_date
        self.order_id = order_id
        self.money = money
        self.province = province
    # 利用魔术方法使得输出为字符串而不是对象地址
    def __str__(self):
        return f"{self.order_date},{self.order_id},{self.money},{self.province}"