import datetime
import sys
from le_alarm import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QTimer
import sqlite3

class Alarm(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


        self.dude = QTimer()
        self.dude.setInterval(1)
        self.dude.timeout.connect(self.check)
        self.dude.start()


        self.dbconnect = sqlite3.connect("data/AlarmDB.db")
        self.cursor = self.dbconnect.cursor()

        self.addbutton.clicked.connect(self.add_to_db)


    def add_to_db(self, value, name):
        self.cursor.execute(f"""insert into alarm (NameofAlarm, DateAndTime) values
        ('{name}', '{value}')""")
        self.cursor.execute("""select * from Alarm order by datetime(DateAndTime)""")
        self.dbconnect.commit()

#    def handle_checks(self):
#        if

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Alarm()
    sys.exit(app.exec_())
