'''
日历控件

QCalendarWidget

'''

import sys,math
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class MyCalendar(QWidget):
    def __init__(self):
        super(MyCalendar, self).__init__()
        self.initUI()
    def initUI(self):
        self.cal = QCalendarWidget(self)
        self.cal.setMinimumDate(QDate(1988,1,1))
        self.cal.setMaximumDate(QDate(2088,1,1))

        self.cal.setGridVisible(True)   # 日历控件网格线是否可见
        self.cal.move(20,20)  # 直接使用绝对定位，没有用那几种布局方法
        self.cal.clicked.connect(self.showDate)
        self.label = QLabel(self)
        date = self.cal.selectedDate()
        self.label.setText(date.toString("yyyy-MM-dd dddd"))  # 年-月-日 星期几
        self.label.move(20,300)

        self.resize(400,350)
        self.setWindowTitle("日历演示")

    def showDate(self,date):
        # 两种方式都可以显示
        #self.label.setText((date.toString("yyyy-MM-dd dddd")))
        self.label.setText((self.cal.selectedDate().toString("yyyy-MM-dd dddd")))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = MyCalendar()
    main.show()
    sys.exit(app.exec_())
