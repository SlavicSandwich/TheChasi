from AlarmDialogLogic import *
from Sound import *
from designs import stopwatchdes, timerdes, Pathetic_Clock, le_alarm
import datetime



# # #################Delet this
#  class Majima(QtWidgets.QMainWindow):                           # <===
#      def __init__(self):
#          super().__init__()
#          self.setWindowTitle("Majima")
#          self.label = QtWidgets.QLabel(self)
#          self.pixmax = QtGui.QPixmap('data/majima bruh.gif')
#          self.label.setPixmap(self.pixmax)
#          self.label.resize(self.pixmax.width(), self.pixmax.height())
#          self.setFixedSize(self.pixmax.width(), self.pixmax.height())
#
#  class Kiryu(QtWidgets.QMainWindow):
#      def __init__(self):
#          super().__init__()
#          self.setWindowTitle("Kiryu")
#          self.label = QtWidgets.QLabel(self)
#          self.pixmax = QtGui.QPixmap('data/kiryu bruh.jpg')
#          self.label.setPixmap(self.pixmax)
#          self.label.resize(self.pixmax.width(), self.pixmax.height())
#          self.setFixedSize(self.pixmax.width(), self.pixmax.height())

######################


class PageWindow(QtWidgets.QMainWindow):
    gotoSignal = QtCore.pyqtSignal(str)

    def goto(self, name):
        self.gotoSignal.emit(name)


class Alarm(PageWindow, le_alarm.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Clockr')
        self.setWindowIcon(QtGui.QIcon('data/logo.png'))
        self.setupUi(self)
        self.timer_switch.clicked.connect(self.gotoTimer)
        self.stopwatch_switch.clicked.connect(self.gotoStopwatch)
        self.worldtime_switch.clicked.connect(self.gotoWorldTime)
        self.Alarm_switch.setDisabled(True)
        self.Alarm_switch.setStyleSheet("background-color: #A3C1DA; color: red;")
        self.select_data()

        self.res = None
        self.melody = 'C:/Users/Slavic Sandwich/PycharmProjects/TheChasi/EEE EEEE.avi'

        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.setSelectionBehavior(self.tableWidget.SelectRows)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.tableWidget.setHorizontalHeaderLabels(['Имя', "Время", "Дни недели", "Активно"])
        self.tableWidget.doubleClicked.connect(self.work)

        self.time_checker = QTimer(self)
        self.time_checker.timeout.connect(self.check_time)
        self.time_checker.start(1)

        self.addbutton.clicked.connect(self.open)

    def work(self):
        data = []
        for idx in self.tableWidget.selectionModel().selectedIndexes():
            data.append(self.tableWidget.item(idx.row(), idx.column()).text())
        self.nig = AlarmDialog(data[0], data[1], data[2], True if data[3] == '1' else False, True)
        self.nig.show()
        self.nig.setModal(True)
        if self.nig.exec_() == QtWidgets.QDialog.Accepted:
            self.select_data()
            connect = sqlite3.connect("data/AlarmDB.db")
            cur = connect.cursor()
            self.res = cur.execute(
                """select NameOfAlarm, Time, DaysOfWeek, IsActive from Alarm where not(id=1)""").fetchall()
        else:
            self.select_data()
            connect = sqlite3.connect("data/AlarmDB.db")
            cur = connect.cursor()
            self.res = cur.execute(
                """select NameOfAlarm, Time, DaysOfWeek, IsActive from Alarm where not(id=1)""").fetchall()

    def open(self):
        self.nig = AlarmDialog()
        self.nig.show()
        if self.nig.exec_() == QtWidgets.QDialog.Accepted:
            self.select_data()
            connect = sqlite3.connect("data/AlarmDB.db")
            cur = connect.cursor()
            self.res = cur.execute(
                """select NameOfAlarm, Time, DaysOfWeek, IsActive from Alarm where not(id=1)""").fetchall()

    def select_data(self):
        connect = sqlite3.connect("data/AlarmDB.db")
        cur = connect.cursor()
        res = cur.execute("""select NameOfAlarm, Time, DaysOfWeek, IsActive from Alarm where not(id=1)""").fetchall()

        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(0)
        for i, row in enumerate(res):
            self.tableWidget.setRowCount(
                self.tableWidget.rowCount() + 1)
            for j, elem in enumerate(row):
                self.tableWidget.setItem(
                    i, j, QTableWidgetItem(str(elem)))

    def check_time(self):
        connect = sqlite3.connect("data/AlarmDB.db")
        cur = connect.cursor()
        res = cur.execute("""select NameOfAlarm, Time, DaysOfWeek, IsActive from Alarm where not(id=1)""").fetchall()
        if res:
            for i in res:
                if i[1].split(':')[0] == datetime.datetime.now().strftime('%H') and \
                        i[1].split(':')[1] == datetime.datetime.now().strftime('%M') \
                        and datetime.datetime.now().strftime('%a') in i[2].split() and i[3]:
                    self.timeup = TimeUp()
                    singleshot = QTimer(self)
                    self.time_checker.stop()
                    singleshot.setSingleShot(True)
                    singleshot.timeout.connect(self.time_checker.start)
                    singleshot.start(60000)
                    self.timeup.exec_()

    def closeEvent(self, event):
        self.connection.close()

    def gotoWorldTime(self):
        self.goto('worldtime')

    def gotoStopwatch(self):
        self.goto('stopwatch')

    def gotoTimer(self):
        self.goto('timer')


class WorldTime(PageWindow, Pathetic_Clock.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Clockr')
        self.setWindowIcon(QtGui.QIcon('data/logo.png'))
        self.setupUi(self)
        self.timer_switch.clicked.connect(self.gotoTimer)
        self.stopwatch_switch.clicked.connect(self.gotoStopwatch)
        self.Alarm_switch.clicked.connect(self.gotoAlarm)
        self.worldtime_switch.setDisabled(True)
        self.worldtime_switch.setStyleSheet("background-color: #A3C1DA; color: red;")

        self.qtimer = QTimer(self)
        self.qtimer.timeout.connect(self.showTime)
        self.qtimer.start(1000)
        font = QtGui.QFont('Arial', 120, QtGui.QFont.Bold)
        self.label.setFont(font)

    def showTime(self):
        current_time = QtCore.QTime.currentTime()
        label_time = current_time.toString('hh:mm:ss')
        self.label.setText(label_time)

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
        self.setWindowTitle('Clockr')
        self.setWindowIcon(QtGui.QIcon('data/logo.png'))

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
                self.timeup = TimeUp()
                self.timeup.exec_()
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
        self.setWindowTitle('Clockr')
        self.setWindowIcon(QtGui.QIcon('data/logo.png'))
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
        self.setWindowTitle('Clockr')
        self.setWindowIcon(QtGui.QIcon('data/logo.png'))
        self.stacked_widget = QtWidgets.QStackedWidget()
        self.setCentralWidget(self.stacked_widget)

        self.m_pages = {}

        self.register(Timer(), "timer")
        self.register(Stopwatch(), "stopwatch")
        self.register(Alarm(), 'alarm')
        self.register(WorldTime(), 'worldtime')

        self.goto("main")

     #############
    # def keyPressEvent(self, event):
    #     if event.key() == PyQt5.Qt.Key_M:
    #         self.Dude = Majima()
    #         self.Dude.show()
    #
    #     if event.key() == PyQt5.Qt.Key_K:
    #         self.Dude = Kiryu()
    #         self.Dude.show()
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


def play_video():
    import pyglet
    import ctypes
    user32 = ctypes.windll.user32
    screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)

    vid_path = 'data/EEE EEEE.avi'  # Name of the video
    window = pyglet.window.Window(600, 600)
    window.set_location(screensize[0] // 2 - 300, screensize[1] // 2 - 300)
    player = pyglet.media.Player()
    source = pyglet.media.StreamingSource()
    MediaLoad = pyglet.media.load(vid_path)

    player.queue(MediaLoad)
    player.play()

    @window.event
    def on_draw():
        if player.source and player.source.video_format:
            player.get_texture().blit(-75, -50)
        else:
            pyglet.app.exit()

    pyglet.app.run()


if __name__ == "__main__":
    import sys

    play_video()
    app = QtWidgets.QApplication(sys.argv)
    w = Window()
    w.show()
    sys.exit(app.exec_())
