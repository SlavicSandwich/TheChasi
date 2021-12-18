from PyQt5 import QtCore, QtWidgets, QtGui
from designs import timerdes, stopwatchdes, workinprogressdes
from PyQt5.QtCore import *

#################Delet this
class Majima(QtWidgets.QMainWindow):                           # <===
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Majima")
        self.label = QtWidgets.QLabel(self)
        self.pixmax = QtGui.QPixmap('data/majima bruh.gif')
        self.label.setPixmap(self.pixmax)
        self.label.resize(self.pixmax.width(), self.pixmax.height())
        self.setFixedSize(self.pixmax.width(), self.pixmax.height())

class Kiryu(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Kiryu")
        self.label = QtWidgets.QLabel(self)
        self.pixmax = QtGui.QPixmap('data/kiryu bruh.jpg')
        self.label.setPixmap(self.pixmax)
        self.label.resize(self.pixmax.width(), self.pixmax.height())
        self.setFixedSize(self.pixmax.width(), self.pixmax.height())

######################


class PageWindow(QtWidgets.QMainWindow):
    gotoSignal = QtCore.pyqtSignal(str)

    def goto(self, name):
        self.gotoSignal.emit(name)

class Alarm(PageWindow, workinprogressdes.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.Alarm_switch.setDisabled(True)
        self.Alarm_switch.setStyleSheet("background-color: #A3C1DA; color: red;")
        qmovie1 = QtGui.QMovie('data/letter-b-dancing.gif')
        qmovie2 = QtGui.QMovie("data/letter-r.gif")
        qmovie3 = QtGui.QMovie('data/letter-u.gif')
        qmovie4 = QtGui.QMovie('data/letter-h.gif')

        self.label_2.setScaledContents(True)
        self.label_3.setScaledContents(True)
        self.label_4.setScaledContents(True)
        self.label_5.setScaledContents(True)

        self.label_2.setMovie(qmovie1)
        self.label_3.setMovie(qmovie2)
        self.label_4.setMovie(qmovie3)
        self.label_5.setMovie(qmovie4)

        qmovie1.start()
        qmovie2.start()
        qmovie3.start()
        qmovie4.start()

        self.timer_switch.clicked.connect(self.gotoTimer)
        self.stopwatch_switch.clicked.connect(self.gotoStopwatch)
        self.worldtime_switch.clicked.connect(self.gotoWorldTime)


    def gotoWorldTime(self):
        self.goto('worldtime')

    def gotoStopwatch(self):
        self.goto('stopwatch')

    def gotoTimer(self):
        self.goto('timer')

class WorldTime(PageWindow, workinprogressdes.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.worldtime_switch.setDisabled(True)
        self.worldtime_switch.setStyleSheet("background-color: #A3C1DA; color: red;")
        qmovie1 = QtGui.QMovie('data/letter-b-dancing.gif')
        qmovie2 = QtGui.QMovie("data/letter-r.gif")
        qmovie3 = QtGui.QMovie('data/letter-u.gif')
        qmovie4 = QtGui.QMovie('data/letter-h.gif')


        self.label_2.setScaledContents(True)
        self.label_3.setScaledContents(True)
        self.label_4.setScaledContents(True)
        self.label_5.setScaledContents(True)

        self.label_2.setMovie(qmovie1)
        self.label_3.setMovie(qmovie2)
        self.label_4.setMovie(qmovie3)
        self.label_5.setMovie(qmovie4)

        qmovie1.start()
        qmovie2.start()
        qmovie3.start()
        qmovie4.start()

        self.timer_switch.clicked.connect(self.gotoTimer)
        self.stopwatch_switch.clicked.connect(self.gotoStopwatch)
        self.Alarm_switch.clicked.connect(self.gotoAlarm)

    def gotoStopwatch(self):
        self.goto('stopwatch')

    def gotoTimer(self):
        self.goto('timer')

    def gotoAlarm(self):
        self.goto('alarm')

class Timer(PageWindow, timerdes.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.flag = False

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.begin_countdown)
        self.timer.start(1000)


        self.pause.hide()
        self.pause.clicked.connect(self.pausecountdown)

        self.pushbutton.clicked.connect(self.button)
        self.stopwatch_switch.clicked.connect(self.gotoStopwatch)
        self.alarm_switch.clicked.connect(self.gotoAlarm)
        self.worldtime_switch.clicked.connect(self.gotoWorldTime)

    def gotoWorldTime(self):
        self.goto('worldtime')

    def gotoStopwatch(self):
        self.goto('stopwatch')

    def gotoAlarm(self):
        self.goto('alarm')

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
            self.pause.setText('Продолжить')
            self.timer.stop()
        else:
            self.pause.setText('Пауза')
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
        self.timer.start()
        self.pause.hide()
        self.pause.setText('Пауза')


class Stopwatch(PageWindow, stopwatchdes.Ui_MainWindow):
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

        self.Alarm_switch.clicked.connect(self.gotoAlarm)
        self.time_switch.clicked.connect(self.gotoTimer)
        self.worldtime_switch.clicked.connect(self.gotoWorldTime)

    def gotoWorldTime(self):
        self.goto('worldtime')

    def gotoTimer(self):
        self.goto('timer')

    def gotoAlarm(self):
        self.goto('alarm')

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


class Window(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setMinimumSize(650, 650)

        self.stacked_widget = QtWidgets.QStackedWidget()
        self.setCentralWidget(self.stacked_widget)

        self.m_pages = {}

        self.register(Timer(), "timer")
        self.register(Stopwatch(), "stopwatch")
        self.register(Alarm(), 'alarm')
        self.register(WorldTime(), 'worldtime')

        self.goto("main")

#############
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_M:
            self.Dude = Majima()
            self.Dude.show()

        if event.key() == Qt.Key_K:
            self.Dude = Kiryu()
            self.Dude.show()
#############Delet this
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
