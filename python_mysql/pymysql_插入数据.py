"""
演示pymysql插入数据的操作
"""
from pymysql import Connection

# 构建到MySQL数据库的连接
conn = Connection(
    host="localhost",       # 主机名/IP地址
    port=3306,              # 端口
    user="root",            # 账号
    password="bear525999",  # 密码
    autocommit=True         # 设置自动提交
)

cur = conn.cursor()     # 获取游标对象
# 选择数据库
conn.select_db("test")
# 执行SQL
# cur.execute("insert into student values(14,'YOYO',24,'女')")
cur.execute("insert into student values(15,'懒羊羊',24,'男')")     # 自动提交
# 通过commit手动确认
# conn.commit()

# 关闭连接
conn.close()