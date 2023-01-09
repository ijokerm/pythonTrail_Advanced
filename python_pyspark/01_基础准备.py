"""
演示获取PySpark的执行环境入口对象：SparkContext
并通过SparkContext对象获取当前PySpark的版本
"""
from pyspark import SparkConf,SparkContext
# 创建SparkConf对象
conf = SparkConf().setMaster("local[*]").setAppName("test_spark_app")
# 基于SparkConf对象创建SparkContext对象
sc = SparkContext(conf=conf)
# 打印PySpark运行版本
print(sc.version)

sc.stop()