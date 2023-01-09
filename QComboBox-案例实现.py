from PyQt5.Qt import *
import sys

class Window(QWidget):
     def __init__(self):
         super().__init__()
         self.setWindowTitle("QComboBox的案例实现")
         self.resize(500,500)
         self.city_dic={"北京":{"东城":"001","西城":'002','朝阳':'003'},
                        "上海":{'黄埔':"005",'徐汇':'006'},
                        "广东":{'广州':"010",'深圳':'011'}}
         self.setup_ui()
     def setup_ui(self):
         #创建两个下拉列表控件
         self.pro=QComboBox(self)
         self.city=QComboBox(self)
         self.pro.move(100,100)
         self.city.move(200,100)
         # 监听省下拉列表里面的当前值发生改变的信号
         self.pro.currentIndexChanged[str].connect(self.pro_change)
         # 监听城市下拉列表里面的当前值发生改变的信号
         self.city.currentIndexChanged.connect(self.city_change)
         #展示数据到第一个下拉列表选择控件中
         self.pro.addItems(self.city_dic.keys())
     def pro_change(self,pro_name):
         # self.city.addItems(self.city_dic[pro_name].values)
         # print(pro_name)
         #根据省的名称，到字典里面，获取对应的城市字典
         citys=self.city_dic[pro_name]
         #临时阻断信号的发射
         self.city.blockSignals(True)
         self.city.clear()
         self.city.blockSignals(False)
         # print(citys)
         #将对应的城市展示到第二个控件里面
         #self.city.addItems(citys.keys())
         for key,val in citys.items():
             self.city.addItem(key,val)

     def city_change(self,index):
         #print(index)
         print(self.city.itemData(index))





if __name__ == '__main__':
     app=QApplication(sys.argv)
     window=Window()
     window.show()
     app.exec_()

