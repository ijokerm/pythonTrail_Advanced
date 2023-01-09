"""
演示RDD的map成员方法使用
"""
from pyspark import SparkConf,SparkContext


conf = SparkConf().setMaster("local[*]").setAppName("create_rdd")
sc = SparkContext(conf=conf)

# 准备一个RDD
rdd = sc.parallelize([('a', 7), ('a', 2), ('b', 2)])
rdd1 = sc.parallelize([2,5,1,8])
rdd2 = sc.parallelize([('a', 2), ('d', 1), ('b', 1)])
rdd3 = sc.parallelize(range(100))
rdd4 = sc.parallelize([('a', ['x', 'y', 'z']), ('b', ['p', 'r'])])
print(rdd.getNumPartitions())

print(sc.version)
print(sc.pythonVer,sc.master,sc.appName,sc.applicationId)

try:
    print(rdd.keys().collect())
except Exception as e:
    print('讨厌的报错',e)
# 通过map方法将全部数据都乘以10
def func(data):
    return data * 10










# (T) -> U 泛型 要求传入一个参数并返回值 不限制类型
# (T) -> T 要求传入和返回的值类型一样
# 链式调用

