# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'stopwatchdes.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(593, 709)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.worldtime_switch = QtWidgets.QPushButton(self.centralwidget)
        self.worldtime_switch.setObjectName("worldtime_switch")
        self.gridLayout.addWidget(self.worldtime_switch, 2, 1, 1, 1)
        self.Alarm_switch = QtWidgets.QPushButton(self.centralwidget)
        self.Alarm_switch.setObjectName("Alarm_switch")
        self.gridLayout.addWidget(self.Alarm_switch, 2, 0, 1, 1)
        self.stopwatch_switch = QtWidgets.QPushButton(self.centralwidget)
        self.stopwatch_switch.setEnabled(False)
        self.stopwatch_switch.setStyleSheet("background-color: #A3C1DA; color: red;")
        self.stopwatch_switch.setCheckable(False)
        self.stopwatch_switch.setObjectName("stopwatch_switch")
        self.gridLayout.addWidget(self.stopwatch_switch, 2, 2, 1, 1)
        self.time_switch = QtWidgets.QPushButton(self.centralwidget)
        self.time_switch.setObjectName("time_switch")
        self.gridLayout.addWidget(self.time_switch, 2, 3, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber.setEnabled(True)
        self.lcdNumber.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lcdNumber.setObjectName("lcdNumber")
        self.verticalLayout_2.addWidget(self.lcdNumber)
        self.beginthing = QtWidgets.QSpinBox(self.centralwidget)
        self.beginthing.setAlignment(QtCore.Qt.AlignCenter)
        self.beginthing.setObjectName("beginthing")
        self.verticalLayout_2.addWidget(self.beginthing)
        self.startbutton = QtWidgets.QPushButton(self.centralwidget)
        self.startbutton.setObjectName("startbutton")
        self.verticalLayout_2.addWidget(self.startbutton)
        self.stopbutton = QtWidgets.QPushButton(self.centralwidget)
        self.stopbutton.setObjectName("stopbutton")
        self.verticalLayout_2.addWidget(self.stopbutton)
        self.resetbutton = QtWidgets.QPushButton(self.centralwidget)
        self.resetbutton.setObjectName("resetbutton")
        self.verticalLayout_2.addWidget(self.resetbutton)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.backwardsstart = QtWidgets.QPushButton(self.groupBox)
        self.backwardsstart.setObjectName("backwardsstart")
        self.verticalLayout.addWidget(self.backwardsstart)
        self.backwardsstopbutton = QtWidgets.QPushButton(self.groupBox)
        self.backwardsstopbutton.setObjectName("backwardsstopbutton")
        self.verticalLayout.addWidget(self.backwardsstopbutton)
        self.verticalLayout_2.addWidget(self.groupBox)
        self.gridLayout.addLayout(self.verticalLayout_2, 1, 0, 1, 4)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 593, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.worldtime_switch.setText(_translate("MainWindow", "Мировое время"))
        self.Alarm_switch.setText(_translate("MainWindow", "Будильник"))
        self.stopwatch_switch.setText(_translate("MainWindow", "Секундомер"))
        self.time_switch.setText(_translate("MainWindow", "Таймер"))
        self.startbutton.setText(_translate("MainWindow", "Старт"))
        self.stopbutton.setText(_translate("MainWindow", "Стоп"))
        self.resetbutton.setText(_translate("MainWindow", "Сбросить"))
        self.groupBox.setTitle(_translate("MainWindow", "Обратный отсчет"))
        self.backwardsstart.setText(_translate("MainWindow", "Старт"))
        self.backwardsstopbutton.setText(_translate("MainWindow", "Стоп"))
