"""
演示pymysql的操作
"""
from pymysql import Connection

# 构建到MySQL数据库的连接
conn = Connection(
    host="localhost",       # 主机名/IP地址
    port=3306,              # 端口
    user="root",            # 账号
    password="bear525999"   # 密码
)

# print(conn.get_server_info())     # mysql数据库的基础信息(版本)
# 执行非查询性质SQL
cur = conn.cursor()     # 获取游标对象
# 选择数据库
conn.select_db("test")
# 执行SQL
# cur.execute("create table test_pymysql(id int,info varchar(100))")
# 执行查询性质SQL
cur.execute("select * from student")
res = cur.fetchall()        # 结果以元祖形式存在
for r in res:
    print(r)

# 关闭连接
conn.close()