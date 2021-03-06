import sys
from PyQt5 import QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QMainWindow
from PIL import ImageQt
from FrontPage import Ui_MainWindow
from ui.model_1 import main as model_1
from ui.model_2 import ImageSegMain as model_2
from ui.model_3 import ImageSegMain as model_3
from ui.model_4 import UserMain as model_4
from  ui.model_5 import UserMain as model_5
class FrontMainEntry(QMainWindow, Ui_MainWindow):
    def __init__(self):

        super().__init__()
        self.setupUi(self)
        self.CutFlag = False
        self.SegmentFlag = False
        # self.pushButton_2.setStyleSheet("QPushButton{border-image: url(shezhi.png)}")
        # self.button.setStyleSheet("QPushButton{background-image: url(img/1.png)}")

        # self.btn.setStyleSheet("QPushButton{border-image: url(shezhi.png)}")
        self.btn.setStyleSheet(
            "QPushButton{color:rgb(0,0,0)}"  # 按键前景色
            "QPushButton{background-color:rgb(255,255,255)}"  # 按键背景色
            "QPushButton:hover{color:red}"  # 光标移动到上面后的前景色
            "QPushButton{border-radius:6px}"  # 圆角半径
            "QPushButton:pressed{background-color:rgb(180,180,180);border: None;}"  # 按下时的样式
            "QPushButton{border-image: url(./icon/tupianchuli.png)}"
        )
        self.btn2.setStyleSheet(
            "QPushButton{color:rgb(0,0,0)}"  # 按键前景色
            "QPushButton{background-color:rgb(255,255,255)}"  # 按键背景色
            "QPushButton:hover{color:red}"  # 光标移动到上面后的前景色
            "QPushButton{border-radius:6px}"  # 圆角半径
            "QPushButton:pressed{background-color:rgb(180,180,180);border: None;}"  # 按下时的样式
            "QPushButton{border-image: url(./icon/图像处理.png)}"
        )
        self.btn3.setStyleSheet(
            "QPushButton{color:rgb(0,0,0)}"  # 按键前景色
            "QPushButton{background-color:rgb(255,255,255)}"  # 按键背景色
            "QPushButton:hover{color:red}"  # 光标移动到上面后的前景色
            "QPushButton{border-radius:6px}"  # 圆角半径
            "QPushButton:pressed{background-color:rgb(180,180,180);border: None;}"  # 按下时的样式
            "QPushButton{border-image: url(./icon/数据处理.png)}"
        )
        self.btn4.setStyleSheet(
            "QPushButton{color:rgb(0,0,0)}"  # 按键前景色
            "QPushButton{background-color:rgb(255,255,255)}"  # 按键背景色
            "QPushButton:hover{color:red}"  # 光标移动到上面后的前景色
            "QPushButton{border-radius:6px}"  # 圆角半径
            "QPushButton:pressed{background-color:rgb(180,180,180);border: None;}"  # 按下时的样式
            "QPushButton{border-image: url(./icon/资源管理.png)}"
        )
        self.btn5.setStyleSheet(
            "QPushButton{color:rgb(0,0,0)}"  # 按键前景色
            "QPushButton{background-color:rgb(255,255,255)}"  # 按键背景色
            "QPushButton:hover{color:red}"  # 光标移动到上面后的前景色
            "QPushButton{border-radius:6px}"  # 圆角半径
            "QPushButton:pressed{background-color:rgb(180,180,180);border: None;}"  # 按下时的样式
            "QPushButton{border-image: url(./icon/用户管理.png)}"
        )
        self.btn6.setStyleSheet(
            "QPushButton{color:rgb(0,0,0)}"  # 按键前景色
            "QPushButton{background-color:rgb(255,255,255)}"  # 按键背景色
            "QPushButton:hover{color:red}"  # 光标移动到上面后的前景色
            "QPushButton{border-radius:6px}"  # 圆角半径
            "QPushButton:pressed{background-color:rgb(180,180,180);border: None;}"  # 按下时的样式
            "QPushButton{border-image: url(./icon/系统设置.png)}"
        )
        self.label.setPixmap(
            ImageQt.toqpixmap("./icon/油田.jpeg").scaled(self.label.size(), Qt.KeepAspectRatio,
                                                                    Qt.SmoothTransformation))

        # self.btn.resize(self.btn.sizeHint())
        # self.btn.setShortcut('L')
        # self.btn.enterEvent()
        self.btn.clicked.connect(self.btnClicked)
        self.btn2.clicked.connect(self.btn2Clicked)
        self.btn4.clicked.connect(self.btn4Clicked)
        self.btn5.clicked.connect(self.btn5Clicked)
        self.btn3.clicked.connect(self.btn3Clicked)
    # def enterEvent(self):
    #     print("鼠标悬停")'
    def btnClicked(self):
        print("模块一 :预处理模块")
        self.WinModel_1=model_1.MyApp()
        self.WinModel_1.show()

    def btn2Clicked(self):
        print("模块二 :图像分割模块")
        self.WinModel_2 = model_2.ImageSegment()
        self.WinModel_2.show()

    def btn3Clicked(self):
        print("模块三 :资源分析模块")
        self.WinModel_3 = model_3.ImageSegment()
        self.WinModel_3.show()

    def btn4Clicked(self):
        print("模块四:资源管理模块")
        self.WinModel_4=model_4.UserApp()
        self.WinModel_4.show()

    def btn5Clicked(self):
        print("模块五:用户管理模块")
        self.WinModel_5=model_5.UserApp()
        self.WinModel_5.show()


# if __name__ == "__main__":
#     app = QtWidgets.QApplication(sys.argv)
#     window = FrontMainEntry()
#
#     window.show()
#     # WinModel_1=model_1.MyApp()
#     # # newWin = NewWindow()
#     # window.btn.clicked.connect(WinModel_1.show)
#     sys.exit(app.exec_())