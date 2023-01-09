"""
面向对象，数据分析案例，主业务逻辑代码
实现步骤：
1、设计一个类可以完成数据的封装
2、设计一个抽象类 定义文件读取的相关功能，并使用子类实现具体功能
3、读取文件生产数据对象
4、进行数据需求的逻辑计算（计算每一天的销售额）
5、通过pyecharts进行图形绘制
"""
from data_define import Record
from file_define import TextFileReader,JsonFileReader,FileReader
from pyecharts.charts import Bar,Timeline
from pyecharts.options import *
from pyecharts.globals import *

txt = TextFileReader("E:/BaiduNetdiskDownload/Python课件/第13章资料/2011年1月销售数据.txt")
Json = JsonFileReader("E:/BaiduNetdiskDownload/Python课件/第13章资料/2011年2月销售数据JSON.txt")
Jan_data:list[Record] = txt.read_data()
Feb_data:list[Record] = Json.read_data()
# 将一二月的数据合并到一张list
all_data:list[Record] = Jan_data + Feb_data

# 计算每一天的销售额 使用字典来存储计算得到的数据，字典的key 不会重复
# 1.判断key是否存在
# 1.1不存在新加一个
# 1.2存在的话 将相同的key对应的value值相加
data_dict = {}          # key:value = date:money
for record in all_data:
    if record.date in data_dict.keys():
        data_dict[record.date] += record.money
    else:
        data_dict[record.date] = record.money

# 可视化图表开发
bar = Bar(init_opts=InitOpts(theme=ThemeType.LIGHT))

bar.add_xaxis(list(data_dict.keys()))   # 添加X轴数据
bar.add_yaxis("销售额",list(data_dict.values()),label_opts=LabelOpts(is_show=False))   # 添加Y轴数据
bar.set_global_opts(
    title_opts=TitleOpts(title="每日销售额")        # 设置标题
)

bar.render("每日销售额柱状图.html")