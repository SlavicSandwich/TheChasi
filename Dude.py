from AlarmDialogLogic import *
from PyQt5.QtWidgets import QApplication, QAbstractItemView
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem
from PyQt5.QtCore import QTimer
from Sound import *
from designs import le_alarm


class DBSAMPLE(QMainWindow, le_alarm.Ui_MainWindow):
    def __init__(self):
        super().__init__()


        self.setupUi(self)
        self.select_data()

        self.res = None

        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.setSelectionBehavior(self.tableWidget.SelectRows)
        self.tableWidget.setHorizontalHeaderLabels(['Имя', "Время", "Дни недели", "Активно"])
        self.tableWidget.doubleClicked.connect(self.work)

        self.time_checker = QTimer(self)
        self.time_checker.timeout.connect(self.check_time)
        self.time_checker.start(1)

        self.AssignSound.clicked.connect(self.assignnSound)

        self.addbutton.clicked.connect(self.open)

    def assignnSound(self):
        global filepath
        self.nig = Why()


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
                    singleshot.start(45000)
                    self.timeup.exec_()



    def closeEvent(self, event):
        self.connection.close()


if __name__ == '__main__':
    print(bool('0'))
    app = QApplication(sys.argv)
    ex = DBSAMPLE()
    ex.show()
    sys.exit(app.exec_())
