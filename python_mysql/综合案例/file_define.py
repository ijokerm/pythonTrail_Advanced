"""
读取/处理 各文件中的数据 并将其封装到list中
"""
import json

from data_define import Record
# 定义父类抽象复写
class FileReader:
    def read_data(self):
        pass
# 处理.txt文件
class TxtFileReader:
    def __init__(self,path):        # 使用构造方法 定义成员变量记录文件路径
        self.path = path
    # 返回值为Record
    def read_data(self) -> list[Record]:
        f = open(self.path,'r',encoding='UTF-8')
        record_list: list[Record] = []
        for r in f.readlines():
            r = r.strip()
            r = r.split(',')
            record = Record(r[0],r[1],r[2],r[3])
            record_list.append(record)
        f.close()
        return record_list
# 处理json文件
class JsonFileReader:
    def __init__(self,path):
        self.path = path

    def read_data(self):
        f = open(self.path,'r',encoding='UTF-8')
        record_list:list[Record] = []
        for line in f.readlines():
            data_dict = json.loads(line)
            record = Record(data_dict['date'],data_dict['order_id'],data_dict["money"],data_dict["province"])
            record_list.append(record)


        f.close()
        return record_list





if __name__ == '__main__':
    txt = TxtFileReader("E:/BaiduNetdiskDownload/Python课件/第13章资料/2011年1月销售数据.txt")
    res = txt.read_data()
    js = JsonFileReader("E:/BaiduNetdiskDownload/Python课件/第13章资料/2011年2月销售数据JSON.txt")
    res2 = js.read_data()
    for l in res2:
        print(l,type(l))
