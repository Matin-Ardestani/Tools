# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'time-picker.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_TimePicker(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(550, 355)
        MainWindow.setStyleSheet("background-color: #F9F9F9;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 550, 200))
        self.frame.setStyleSheet("border: none;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(96, 50, 51, 17))
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(13)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(242, 50, 65, 17))
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(13)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(385, 50, 71, 17))
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(13)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.select_hour = QtWidgets.QComboBox(self.frame)
        self.select_hour.setGeometry(QtCore.QRect(80, 90, 86, 25))
        font = QtGui.QFont()
        font.setFamily("Sawasdee")
        font.setPointSize(13)
        self.select_hour.setFont(font)
        self.select_hour.setStyleSheet("background-color: #DEDEDE;\n"
"color: #0B0D12;\n"
"border-radius: 4px;")
        self.select_hour.setObjectName("select_hour")
        self.select_hour.addItem("")
        self.select_hour.addItem("")
        self.select_hour.addItem("")
        self.select_hour.addItem("")
        self.select_hour.addItem("")
        self.select_hour.addItem("")
        self.select_hour.addItem("")
        self.select_hour.addItem("")
        self.select_hour.addItem("")
        self.select_hour.addItem("")
        self.select_hour.addItem("")
        self.select_hour.addItem("")
        self.select_hour.addItem("")
        self.select_hour.addItem("")
        self.select_hour.addItem("")
        self.select_hour.addItem("")
        self.select_hour.addItem("")
        self.select_hour.addItem("")
        self.select_hour.addItem("")
        self.select_hour.addItem("")
        self.select_hour.addItem("")
        self.select_hour.addItem("")
        self.select_hour.addItem("")
        self.select_hour.addItem("")
        self.select_minute = QtWidgets.QComboBox(self.frame)
        self.select_minute.setGeometry(QtCore.QRect(230, 90, 86, 25))
        font = QtGui.QFont()
        font.setFamily("Sawasdee")
        font.setPointSize(13)
        self.select_minute.setFont(font)
        self.select_minute.setStyleSheet("background-color: #DEDEDE;\n"
"color: #0B0D12;\n"
"border-radius: 4px;")
        self.select_minute.setObjectName("select_minute")
        self.select_minute.addItem("")
        self.select_minute.addItem("")
        self.select_minute.addItem("")
        self.select_minute.addItem("")
        self.select_minute.addItem("")
        self.select_minute.addItem("")
        self.select_minute.addItem("")
        self.select_minute.addItem("")
        self.select_minute.addItem("")
        self.select_minute.addItem("")
        self.select_minute.addItem("")
        self.select_minute.addItem("")
        self.select_minute.addItem("")
        self.select_minute.addItem("")
        self.select_minute.addItem("")
        self.select_minute.addItem("")
        self.select_minute.addItem("")
        self.select_minute.addItem("")
        self.select_minute.addItem("")
        self.select_minute.addItem("")
        self.select_minute.addItem("")
        self.select_minute.addItem("")
        self.select_minute.addItem("")
        self.select_minute.addItem("")
        self.select_minute.addItem("")
        self.select_minute.addItem("")
        self.select_minute.addItem("")
        self.select_minute.addItem("")
        self.select_minute.addItem("")
        self.select_minute.addItem("")
        self.select_minute.addItem("")
        self.select_minute.addItem("")
        self.select_minute.addItem("")
        self.select_minute.addItem("")
        self.select_minute.addItem("")
        self.select_minute.addItem("")
        self.select_minute.addItem("")
        self.select_minute.addItem("")
        self.select_minute.addItem("")
        self.select_minute.addItem("")
        self.select_minute.addItem("")
        self.select_minute.addItem("")
        self.select_minute.addItem("")
        self.select_minute.addItem("")
        self.select_minute.addItem("")
        self.select_minute.addItem("")
        self.select_minute.addItem("")
        self.select_minute.addItem("")
        self.select_minute.addItem("")
        self.select_minute.addItem("")
        self.select_minute.addItem("")
        self.select_minute.addItem("")
        self.select_minute.addItem("")
        self.select_minute.addItem("")
        self.select_minute.addItem("")
        self.select_minute.addItem("")
        self.select_minute.addItem("")
        self.select_minute.addItem("")
        self.select_minute.addItem("")
        self.select_minute.addItem("")
        self.select_second = QtWidgets.QComboBox(self.frame)
        self.select_second.setGeometry(QtCore.QRect(376, 90, 86, 25))
        font = QtGui.QFont()
        font.setFamily("Sawasdee")
        font.setPointSize(13)
        self.select_second.setFont(font)
        self.select_second.setStyleSheet("background-color: #DEDEDE;\n"
"color: #0B0D12;\n"
"border-radius: 4px;")
        self.select_second.setObjectName("select_second")
        self.select_second.addItem("")
        self.select_second.addItem("")
        self.select_second.addItem("")
        self.select_second.addItem("")
        self.select_second.addItem("")
        self.select_second.addItem("")
        self.select_second.addItem("")
        self.select_second.addItem("")
        self.select_second.addItem("")
        self.select_second.addItem("")
        self.select_second.addItem("")
        self.select_second.addItem("")
        self.select_second.addItem("")
        self.select_second.addItem("")
        self.select_second.addItem("")
        self.select_second.addItem("")
        self.select_second.addItem("")
        self.select_second.addItem("")
        self.select_second.addItem("")
        self.select_second.addItem("")
        self.select_second.addItem("")
        self.select_second.addItem("")
        self.select_second.addItem("")
        self.select_second.addItem("")
        self.select_second.addItem("")
        self.select_second.addItem("")
        self.select_second.addItem("")
        self.select_second.addItem("")
        self.select_second.addItem("")
        self.select_second.addItem("")
        self.select_second.addItem("")
        self.select_second.addItem("")
        self.select_second.addItem("")
        self.select_second.addItem("")
        self.select_second.addItem("")
        self.select_second.addItem("")
        self.select_second.addItem("")
        self.select_second.addItem("")
        self.select_second.addItem("")
        self.select_second.addItem("")
        self.select_second.addItem("")
        self.select_second.addItem("")
        self.select_second.addItem("")
        self.select_second.addItem("")
        self.select_second.addItem("")
        self.select_second.addItem("")
        self.select_second.addItem("")
        self.select_second.addItem("")
        self.select_second.addItem("")
        self.select_second.addItem("")
        self.select_second.addItem("")
        self.select_second.addItem("")
        self.select_second.addItem("")
        self.select_second.addItem("")
        self.select_second.addItem("")
        self.select_second.addItem("")
        self.select_second.addItem("")
        self.select_second.addItem("")
        self.select_second.addItem("")
        self.select_second.addItem("")
        self.select_btn = QtWidgets.QPushButton(self.centralwidget)
        self.select_btn.setGeometry(QtCore.QRect(200, 250, 150, 50))
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(13)
        self.select_btn.setFont(font)
        self.select_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.select_btn.setStyleSheet("background-color: #DEDEDE;\n"
"color: #0B0D12;\n"
"border-radius: 4px;")
        self.select_btn.setObjectName("select_btn")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Choose Time"))
        self.label.setText(_translate("MainWindow", "Hour:"))
        self.label_2.setText(_translate("MainWindow", "Minute:"))
        self.label_3.setText(_translate("MainWindow", "Second:"))
        self.select_hour.setItemText(0, _translate("MainWindow", "00"))
        self.select_hour.setItemText(1, _translate("MainWindow", "01"))
        self.select_hour.setItemText(2, _translate("MainWindow", "02"))
        self.select_hour.setItemText(3, _translate("MainWindow", "03"))
        self.select_hour.setItemText(4, _translate("MainWindow", "04"))
        self.select_hour.setItemText(5, _translate("MainWindow", "05"))
        self.select_hour.setItemText(6, _translate("MainWindow", "06"))
        self.select_hour.setItemText(7, _translate("MainWindow", "07"))
        self.select_hour.setItemText(8, _translate("MainWindow", "08"))
        self.select_hour.setItemText(9, _translate("MainWindow", "09"))
        self.select_hour.setItemText(10, _translate("MainWindow", "10"))
        self.select_hour.setItemText(11, _translate("MainWindow", "11"))
        self.select_hour.setItemText(12, _translate("MainWindow", "12"))
        self.select_hour.setItemText(13, _translate("MainWindow", "13"))
        self.select_hour.setItemText(14, _translate("MainWindow", "14"))
        self.select_hour.setItemText(15, _translate("MainWindow", "15"))
        self.select_hour.setItemText(16, _translate("MainWindow", "16"))
        self.select_hour.setItemText(17, _translate("MainWindow", "17"))
        self.select_hour.setItemText(18, _translate("MainWindow", "18"))
        self.select_hour.setItemText(19, _translate("MainWindow", "19"))
        self.select_hour.setItemText(20, _translate("MainWindow", "20"))
        self.select_hour.setItemText(21, _translate("MainWindow", "21"))
        self.select_hour.setItemText(22, _translate("MainWindow", "22"))
        self.select_hour.setItemText(23, _translate("MainWindow", "23"))
        self.select_minute.setItemText(0, _translate("MainWindow", "00"))
        self.select_minute.setItemText(1, _translate("MainWindow", "01"))
        self.select_minute.setItemText(2, _translate("MainWindow", "02"))
        self.select_minute.setItemText(3, _translate("MainWindow", "03"))
        self.select_minute.setItemText(4, _translate("MainWindow", "04"))
        self.select_minute.setItemText(5, _translate("MainWindow", "05"))
        self.select_minute.setItemText(6, _translate("MainWindow", "06"))
        self.select_minute.setItemText(7, _translate("MainWindow", "07"))
        self.select_minute.setItemText(8, _translate("MainWindow", "08"))
        self.select_minute.setItemText(9, _translate("MainWindow", "09"))
        self.select_minute.setItemText(10, _translate("MainWindow", "10"))
        self.select_minute.setItemText(11, _translate("MainWindow", "11"))
        self.select_minute.setItemText(12, _translate("MainWindow", "12"))
        self.select_minute.setItemText(13, _translate("MainWindow", "13"))
        self.select_minute.setItemText(14, _translate("MainWindow", "14"))
        self.select_minute.setItemText(15, _translate("MainWindow", "15"))
        self.select_minute.setItemText(16, _translate("MainWindow", "16"))
        self.select_minute.setItemText(17, _translate("MainWindow", "17"))
        self.select_minute.setItemText(18, _translate("MainWindow", "18"))
        self.select_minute.setItemText(19, _translate("MainWindow", "19"))
        self.select_minute.setItemText(20, _translate("MainWindow", "20"))
        self.select_minute.setItemText(21, _translate("MainWindow", "21"))
        self.select_minute.setItemText(22, _translate("MainWindow", "22"))
        self.select_minute.setItemText(23, _translate("MainWindow", "23"))
        self.select_minute.setItemText(24, _translate("MainWindow", "24"))
        self.select_minute.setItemText(25, _translate("MainWindow", "25"))
        self.select_minute.setItemText(26, _translate("MainWindow", "26"))
        self.select_minute.setItemText(27, _translate("MainWindow", "27"))
        self.select_minute.setItemText(28, _translate("MainWindow", "28"))
        self.select_minute.setItemText(29, _translate("MainWindow", "29"))
        self.select_minute.setItemText(30, _translate("MainWindow", "30"))
        self.select_minute.setItemText(31, _translate("MainWindow", "31"))
        self.select_minute.setItemText(32, _translate("MainWindow", "32"))
        self.select_minute.setItemText(33, _translate("MainWindow", "33"))
        self.select_minute.setItemText(34, _translate("MainWindow", "34"))
        self.select_minute.setItemText(35, _translate("MainWindow", "35"))
        self.select_minute.setItemText(36, _translate("MainWindow", "36"))
        self.select_minute.setItemText(37, _translate("MainWindow", "37"))
        self.select_minute.setItemText(38, _translate("MainWindow", "38"))
        self.select_minute.setItemText(39, _translate("MainWindow", "39"))
        self.select_minute.setItemText(40, _translate("MainWindow", "40"))
        self.select_minute.setItemText(41, _translate("MainWindow", "41"))
        self.select_minute.setItemText(42, _translate("MainWindow", "42"))
        self.select_minute.setItemText(43, _translate("MainWindow", "43"))
        self.select_minute.setItemText(44, _translate("MainWindow", "44"))
        self.select_minute.setItemText(45, _translate("MainWindow", "45"))
        self.select_minute.setItemText(46, _translate("MainWindow", "46"))
        self.select_minute.setItemText(47, _translate("MainWindow", "47"))
        self.select_minute.setItemText(48, _translate("MainWindow", "48"))
        self.select_minute.setItemText(49, _translate("MainWindow", "49"))
        self.select_minute.setItemText(50, _translate("MainWindow", "50"))
        self.select_minute.setItemText(51, _translate("MainWindow", "51"))
        self.select_minute.setItemText(52, _translate("MainWindow", "52"))
        self.select_minute.setItemText(53, _translate("MainWindow", "53"))
        self.select_minute.setItemText(54, _translate("MainWindow", "54"))
        self.select_minute.setItemText(55, _translate("MainWindow", "55"))
        self.select_minute.setItemText(56, _translate("MainWindow", "56"))
        self.select_minute.setItemText(57, _translate("MainWindow", "57"))
        self.select_minute.setItemText(58, _translate("MainWindow", "58"))
        self.select_minute.setItemText(59, _translate("MainWindow", "59"))
        self.select_second.setItemText(0, _translate("MainWindow", "00"))
        self.select_second.setItemText(1, _translate("MainWindow", "01"))
        self.select_second.setItemText(2, _translate("MainWindow", "02"))
        self.select_second.setItemText(3, _translate("MainWindow", "03"))
        self.select_second.setItemText(4, _translate("MainWindow", "04"))
        self.select_second.setItemText(5, _translate("MainWindow", "05"))
        self.select_second.setItemText(6, _translate("MainWindow", "06"))
        self.select_second.setItemText(7, _translate("MainWindow", "07"))
        self.select_second.setItemText(8, _translate("MainWindow", "08"))
        self.select_second.setItemText(9, _translate("MainWindow", "09"))
        self.select_second.setItemText(10, _translate("MainWindow", "10"))
        self.select_second.setItemText(11, _translate("MainWindow", "11"))
        self.select_second.setItemText(12, _translate("MainWindow", "12"))
        self.select_second.setItemText(13, _translate("MainWindow", "13"))
        self.select_second.setItemText(14, _translate("MainWindow", "14"))
        self.select_second.setItemText(15, _translate("MainWindow", "15"))
        self.select_second.setItemText(16, _translate("MainWindow", "16"))
        self.select_second.setItemText(17, _translate("MainWindow", "17"))
        self.select_second.setItemText(18, _translate("MainWindow", "18"))
        self.select_second.setItemText(19, _translate("MainWindow", "19"))
        self.select_second.setItemText(20, _translate("MainWindow", "20"))
        self.select_second.setItemText(21, _translate("MainWindow", "21"))
        self.select_second.setItemText(22, _translate("MainWindow", "22"))
        self.select_second.setItemText(23, _translate("MainWindow", "23"))
        self.select_second.setItemText(24, _translate("MainWindow", "24"))
        self.select_second.setItemText(25, _translate("MainWindow", "25"))
        self.select_second.setItemText(26, _translate("MainWindow", "26"))
        self.select_second.setItemText(27, _translate("MainWindow", "27"))
        self.select_second.setItemText(28, _translate("MainWindow", "28"))
        self.select_second.setItemText(29, _translate("MainWindow", "29"))
        self.select_second.setItemText(30, _translate("MainWindow", "30"))
        self.select_second.setItemText(31, _translate("MainWindow", "31"))
        self.select_second.setItemText(32, _translate("MainWindow", "32"))
        self.select_second.setItemText(33, _translate("MainWindow", "33"))
        self.select_second.setItemText(34, _translate("MainWindow", "34"))
        self.select_second.setItemText(35, _translate("MainWindow", "35"))
        self.select_second.setItemText(36, _translate("MainWindow", "36"))
        self.select_second.setItemText(37, _translate("MainWindow", "37"))
        self.select_second.setItemText(38, _translate("MainWindow", "38"))
        self.select_second.setItemText(39, _translate("MainWindow", "39"))
        self.select_second.setItemText(40, _translate("MainWindow", "40"))
        self.select_second.setItemText(41, _translate("MainWindow", "41"))
        self.select_second.setItemText(42, _translate("MainWindow", "42"))
        self.select_second.setItemText(43, _translate("MainWindow", "43"))
        self.select_second.setItemText(44, _translate("MainWindow", "44"))
        self.select_second.setItemText(45, _translate("MainWindow", "45"))
        self.select_second.setItemText(46, _translate("MainWindow", "46"))
        self.select_second.setItemText(47, _translate("MainWindow", "47"))
        self.select_second.setItemText(48, _translate("MainWindow", "48"))
        self.select_second.setItemText(49, _translate("MainWindow", "49"))
        self.select_second.setItemText(50, _translate("MainWindow", "50"))
        self.select_second.setItemText(51, _translate("MainWindow", "51"))
        self.select_second.setItemText(52, _translate("MainWindow", "52"))
        self.select_second.setItemText(53, _translate("MainWindow", "53"))
        self.select_second.setItemText(54, _translate("MainWindow", "54"))
        self.select_second.setItemText(55, _translate("MainWindow", "55"))
        self.select_second.setItemText(56, _translate("MainWindow", "56"))
        self.select_second.setItemText(57, _translate("MainWindow", "57"))
        self.select_second.setItemText(58, _translate("MainWindow", "58"))
        self.select_second.setItemText(59, _translate("MainWindow", "59"))
        self.select_btn.setText(_translate("MainWindow", "Select"))