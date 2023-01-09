"""
演示闭包
"""
# 简单闭包演示
def outer(logo):

    def inner(msg):
        print(f"<{logo}>{msg}<{logo}>")

    return inner

fn = outer("test")   # fn--确定了logo变量为test的inner函数
fn("bear")

# 使用闭包实现ATM存取功能
def outer_money(money=0):

    def inner_atm(num,deposit):
        nonlocal money        # 需要使用nonlocal关键字修饰外部函数的变量 才可在内部函数中修改它
        if deposit:
            money += num
            print(f"存款{num}元，余额{money}元")
        else:
            money -= num
            print(f"取款{num}元，余额{money}元")

    return inner_atm  # 必须要返回内部函数名 否则报错TypeError: 'NoneType' object is not callable

atm = outer_money(200)
atm(300,True)
