"""
和文件相关的类定义 处理文件中的数据（此时是Record对象）
"""
import json

from data_define import Record
# 定义一个抽象类 确定有哪些功能需要实现
class FileReader:
    def read_data(self) -> list[Record]:
        """读取文件的数据，读到的每条数据都转化为Record对象，封装到list内返回"""
        pass

class TextFileReader(FileReader):

    def __init__(self,path):
        self.path = path    # 定义成员变量 记录文件路径

    # 复写（实现）抽象方法
    def read_data(self) -> list[Record]:
        f = open(self.path,'r',encoding='UTF-8')
        record_list: list[Record] = []
        for line in f.readlines():
            line = line.strip()     # 消除读取到的换行\n
            data_list = line.split(",")
            record = Record(data_list[0],data_list[1],int(data_list[2]),data_list[3])
            record_list.append(record)

        f.close()
        return record_list

class JsonFileReader:
    def __init__(self,path):
        self.path = path    # 定义成员变量 记录文件路径

     # 复写（实现）抽象方法
    def read_data(self) -> list[Record]:
        f = open(self.path, 'r', encoding='UTF-8')
        record_list: list[Record] = []
        for line in f.readlines():
            data_dict = json.loads(line)
            record = Record(data_dict["date"],data_dict["order_id"],int(data_dict["money"]),data_dict["province"])
            record_list.append(record)

        f.close()
        return record_list
if __name__ == '__main__':
    textfile_reader = TextFileReader("E:/BaiduNetdiskDownload/Python课件/第13章资料/2011年1月销售数据.txt")
    jsonfile_reader = JsonFileReader("E:/BaiduNetdiskDownload/Python课件/第13章资料/2011年2月销售数据JSON.txt")
    textlist = textfile_reader.read_data()
    jsonlist = jsonfile_reader.read_data()
    for l1 in jsonlist:
        print(l1)


