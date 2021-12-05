from PyQt5 import QtCore, QtWidgets
from designs import stopwatchdes, timerdes
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class PageWindow(QtWidgets.QMainWindow):
    gotoSignal = QtCore.pyqtSignal(str)

    def goto(self, name):
        self.gotoSignal.emit(name)


class Stopwatch(PageWindow, stopwatchdes.Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.time = [0, 0]
        self.timeinterwal = 10

        self.timer = QTimer()
        self.timer.setInterval(self.timeinterwal)
        self.timer.timeout.connect(self.updateTime)

        self.timeddown = QTimer()
        self.timeddown.setInterval(self.timeinterwal)
        self.timeddown.timeout.connect(self.updatedowntime)

        self.startbutton.clicked.connect(self.timer.start)
        self.stopbutton.clicked.connect(self.timer.stop)
        self.resetbutton.clicked.connect(self.reset)
        self.beginthing.valueChanged.connect(self.set_beginning)
        self.backwardsstart.clicked.connect(self.timeddown.start)
        self.backwardsstopbutton.clicked.connect(self.timeddown.stop)

        self.switcher = QPushButton(self)
        self.switcher.setText('Перелистнуть')
        self.switcher.move(30, 300)
        self.switcher.clicked.connect(self.gotoSearch)

    def gotoSearch(self):
        self.goto('search')

    def set_beginning(self):
        self.time[0] = self.beginthing.value()
        self.lcdNumber.display(str(self.time[0]) + '.' + str(self.time[1]))

    def settimer(self, str):
        self.lcdNumber.display(str)

    def reset(self):
        self.beginthing.setValue(0)
        self.time = [0, 0]
        self.settimer(str(self.time[0]) + '.' + str(self.time[1]))
        self.backwardsstart.setEnabled(True)
        self.backwardsstopbutton.setEnabled(True)
        self.startbutton.setEnabled(True)
        self.stopbutton.setEnabled(True)

    def updatedowntime(self):
        self.startbutton.setDisabled(True)
        self.stopbutton.setDisabled(True)
        if self.time[1] > 0:
            self.time[1] -= 1
        else:
            self.time[1] = 100
            self.time[0] -= 1
        self.settimer(str(self.time[0]) + '.' + str(self.time[1]))

    def updateTime(self):
        self.backwardsstart.setDisabled(True)
        self.backwardsstopbutton.setDisabled(True)
        if self.time[1] < 99:
            self.time[1] += 1
        else:
            self.time[0] += 1
            self.time[1] = 0
        self.settimer(str(self.time[0]) + '.' + str(self.time[1]))


class Timer(PageWindow, timerdes.Ui_Form):
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

        self.switch = QPushButton(self)
        self.switch.setText('Перелистнуть')
        self.switch.setGeometry(QtCore.QRect(50, 300, 80, 25))
        self.switch.clicked.connect(self.gotoMain)

        self.pushbutton.clicked.connect(self.button)

    def gotoMain(self):
        self.goto('main')

    def button(self):
        if self.pushbutton.text() == 'Старт':
            self.flag = True
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


class Window(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.stacked_widget = QtWidgets.QStackedWidget()
        self.setCentralWidget(self.stacked_widget)

        self.m_pages = {}

        self.register(Timer(), "main")
        self.register(Stopwatch(), "search")

        self.goto("main")

    def register(self, widget, name):
        self.m_pages[name] = widget
        self.stacked_widget.addWidget(widget)
        if isinstance(widget, PageWindow):
            widget.gotoSignal.connect(self.goto)

    @QtCore.pyqtSlot(str)
    def goto(self, name):
        if name in self.m_pages:
            widget = self.m_pages[name]
            self.stacked_widget.setCurrentWidget(widget)
            self.setWindowTitle(widget.windowTitle())


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    w = Window()
    w.show()
    sys.exit(app.exec_())
