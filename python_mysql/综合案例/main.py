"""
实现将面向对象中的数据.txt/.json利用pymysql写入数据库表单中
实现过程：
1.复用面向对象代码 --读取数据 封装数据对象
2.构建数据库连接
3.写入数据库
"""
from data_define import Record
from file_define import *
from pymysql import Connection

txtfile = TxtFileReader("E:/BaiduNetdiskDownload/Python课件/第13章资料/2011年1月销售数据.txt")
jsonfile = JsonFileReader("E:/BaiduNetdiskDownload/Python课件/第13章资料/2011年2月销售数据JSON.txt")
Jan_data = txtfile.read_data()
Feb_data = jsonfile.read_data()
# 合并一月二月数据
all_data = Jan_data + Feb_data

# 构建数据库连接
conn = Connection(
    host='localhost',
    port=3306,
    user="root",
    password='bear525999',
    autocommit=True
)
# 构建游标对象
cur = conn.cursor()
# 选择数据库
conn.select_db("py_sql")
# 写入数据库
for record in all_data:
    sql = "insert into orders(order_date,order_id,money,province) " \
          f"values ('{record.order_date}','{record.order_id}',{record.money},'{record.province}')"
    cur.execute(sql)

conn.close()




