import sys
from designs.le_alarm import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QTimer
import sqlite3


class Alarm(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.dude = QTimer()
        self.dude.setInterval(1)
        # self.dude.timeout.connect(self.check)
        self.dude.start()

        self.dbconnect = sqlite3.connect("data/AlarmDB.db")
        self.cursor = self.dbconnect.cursor()

        self.addbutton.clicked.connect(self.add_to_db)

    def add_to_db(self, value, name):
        self.cursor.execute(f"""insert into alarm (NameofAlarm, DateAndTime) values
        ('{name}', '{value}')""")
        self.cursor.execute("""select * from Alarm order by datetime(DateAndTime)""")
        self.dbconnect.commit()

    def select_data(self):
        res = self.cursor.execute('select from Alarm')
        # Заполним размеры таблицы
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(0)
        # Заполняем таблицу элементами
        for i, row in enumerate(res):
            self.tableWidget.setRowCount(
                self.tableWidget.rowCount() + 1)
            for j, elem in enumerate(row):
                self.tableWidget.setItem(
                    i, j, QTableWidgetItem(str(elem)))


#    def handle_checks(self):
#        if

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Alarm()
    ex.show()
    sys.exit(app.exec_())