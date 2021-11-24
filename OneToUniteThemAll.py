from PyQt5 import QtCore, QtWidgets
from designs import stopwatch, timerdes
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class PageWindow(QtWidgets.QMainWindow):
    gotoSignal = QtCore.pyqtSignal(str)

    def goto(self, name):
        self.gotoSignal.emit(name)


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
        self.switch.clicked.connect(self.gotoSearch)

        self.pushbutton.clicked.connect(self.button)

    def gotoSearch(self):
        self.goto('search')

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


class Stopwatch(PageWindow, stopwatch.Ui_Form):
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
