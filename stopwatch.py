from designs.stopwatch import *
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QTimer


class Stopwatch(QMainWindow, Ui_Form):
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


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Stopwatch()
    ex.show()
    sys.exit(app.exec_())
