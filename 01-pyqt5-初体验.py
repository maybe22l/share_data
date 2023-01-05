from PyQt5.Qt import * #主要包含了一些我们常用的一些类，汇总到了一块
import sys
app=QApplication(sys.argv)
window=QWidget()#QWidget是一个最简单的空白控件，是所有可视控件的基类

window.setWindowTitle("第一个界面测试")#设置窗体的标题文字
window.resize(500,500)#设置窗体的宽度和高度
window.move(600,200)
label=QLabel('hello world',window)#创建标签，父容器为window,第一个参数为内容，第二个参数为父容器
#label.setText("hello world")#设置标签文字
label.move(200,200)
#label.setGeometry(200,200,300,300)#位置以及宽和高
btn=QPushButton("按钮")#创建按钮
btn.setParent(window)#按钮的父容器是当前窗口
#创建字体对象
font=QFont()
font.setPointSize(14)#设置字体大小
font.setBold(True)#设置字体为粗体
label.setFont(font)#将其字体设置为标签的字体

#调整窗口在屏幕中央显示
center_pointer=QDesktopWidget().availableGeometry().center()
print(center_pointer)#输出可用屏幕中心点
x=center_pointer.x()
y=center_pointer.y()
“”“”“进行改变la啦啦啦啦啦啦啦
sys.exit(app.exec_())#应用程序运行
