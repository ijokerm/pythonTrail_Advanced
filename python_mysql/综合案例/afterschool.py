"""
将我们写入到MySQL的数据，通过Python代码读取出来
在反向写出为如下图的文件 json格式
"""
import json

from pymysql import Connection

conn = Connection(
    host='localhost',
    port=3306,
    user='root',
    password='bear525999'
)

cur = conn.cursor()
conn.select_db('py_sql')
cur.execute("select * from orders")
res = cur.fetchall()    # 结果以元组形式存在
data_dict = {}
for r in res:
    data_dict['date'] = str(r[0])
    data_dict["order_id"] = r[1]
    data_dict["money"] = r[2]
    data_dict["province"] = r[3]
    print(data_dict)



conn.close()