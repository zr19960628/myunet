# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainForm.ui'
#
# Created by: PyQt5 ui code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1050, 773)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_InputImg = QtWidgets.QLabel(self.centralwidget)
        self.label_InputImg.setGeometry(QtCore.QRect(30, 160, 512, 512))
        self.label_InputImg.setAlignment(QtCore.Qt.AlignCenter)
        self.label_InputImg.setObjectName("label_InputImg")
        self.label_CutImg = QtWidgets.QLabel(self.centralwidget)
        self.label_CutImg.setGeometry(QtCore.QRect(600, 150, 256, 256))
        self.label_CutImg.setAlignment(QtCore.Qt.AlignCenter)
        self.label_CutImg.setObjectName("label_CutImg")
        self.label_SegImg = QtWidgets.QLabel(self.centralwidget)
        self.label_SegImg.setGeometry(QtCore.QRect(600, 430, 256, 256))
        self.label_SegImg.setAlignment(QtCore.Qt.AlignCenter)
        self.label_SegImg.setObjectName("label_SegImg")
        self.pushButton_Open = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Open.setGeometry(QtCore.QRect(550, 80, 75, 23))
        self.pushButton_Open.setObjectName("pushButton_Open")
        self.pushButton__Cut = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton__Cut.setGeometry(QtCore.QRect(650, 80, 75, 23))
        self.pushButton__Cut.setObjectName("pushButton__Cut")
        self.pushButton_Segment = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Segment.setGeometry(QtCore.QRect(750, 80, 75, 23))
        self.pushButton_Segment.setObjectName("pushButton_Segment")
        self.pushButton_Save = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Save.setGeometry(QtCore.QRect(850, 80, 75, 23))
        self.pushButton_Save.setObjectName("pushButton_Save")
        self.label_ImgPath = QtWidgets.QLabel(self.centralwidget)
        self.label_ImgPath.setGeometry(QtCore.QRect(225, 85, 54, 12))
        self.label_ImgPath.setObjectName("label_ImgPath")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(290, 80, 241, 20))
        self.lineEdit.setObjectName("lineEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1050, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton_Open.clicked.connect(MainWindow.btnOpen_Clicked)
        self.pushButton__Cut.clicked.connect(MainWindow.btnCut_Clicked)
        self.pushButton_Segment.clicked.connect(MainWindow.btnSegment_Clicked)
        self.pushButton_Save.clicked.connect(MainWindow.btnSave_Clicked)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_InputImg.setText(_translate("MainWindow", "输入图片"))
        self.label_CutImg.setText(_translate("MainWindow", "切分图片"))
        self.label_SegImg.setText(_translate("MainWindow", "分割图片"))
        self.pushButton_Open.setText(_translate("MainWindow", "打开"))
        self.pushButton__Cut.setText(_translate("MainWindow", "切分"))
        self.pushButton_Segment.setText(_translate("MainWindow", "分割"))
        self.pushButton_Save.setText(_translate("MainWindow", "保存"))
        self.label_ImgPath.setText(_translate("MainWindow", "图片路径"))