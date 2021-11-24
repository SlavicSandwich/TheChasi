from designs.timerdes import *
import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5.QtCore import *


class Timer(QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.flag = False

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.begin_countdown)
        self.timer.start(1000)

        self.pause = QPushButton(self)
        self.pause.setText('Пауза')
        self.pause.setGeometry(QtCore.QRect(60, 200, 121, 23))
        self.pause.setObjectName("pausebutton")
        self.pause.hide()
        self.pause.clicked.connect(self.pausecountdown)

        self.pushbutton.clicked.connect(self.button)

    def button(self):
        if self.pushbutton.text() == 'Старт':
            self.flag= True
            self.pushbutton.setText('Стоп')
            self.begin_countdown()
        elif self.pushbutton.text() == 'Стоп':
            self.reset()


    def begin_countdown(self):
        if self.flag:
            self.hourbox.setDisabled(True)
            self.minbox.setDisabled(True)
            self.secondbox.setDisabled(True)
            self.pause.show()
            if int(self.secondbox.value()) != 0:
                self.secondbox.setValue(int(self.secondbox.value() - 1))
            elif int(self.secondbox.value()) == 0 and int(self.minbox.value()) != 0:
                self.minbox.setValue(int(self.minbox.value()) - 1)
                self.secondbox.setValue(59)

            elif int(self.secondbox.value()) == 0 and int(self.minbox.value()) == 0 and int(self.hourbox.value()) != 0:
                self.hourbox.setValue(int(self.hourbox.value()) - 1)
                self.minbox.setValue(59)
                self.secondbox.setValue(59)

            else:
                self.reset()

    def pausecountdown(self):
        if self.timer.isActive():
            self.timer.stop()
        else:
            self.timer.start()

    def reset(self):
        self.flag = False
        self.pushbutton.setText('Старт')
        self.hourbox.setDisabled(False)
        self.hourbox.setValue(0)
        self.minbox.setDisabled(False)
        self.minbox.setValue(0)
        self.secondbox.setDisabled(False)
        self.secondbox.setValue(0)
        self.pause.hide()


App = QApplication(sys.argv)

# create the instance of our Window
window = Timer()
window.show()

# start the app
sys.exit(App.exec())