from Dude import *
from designs import AlarmDialog
from PyQt5.QtWidgets import *
import sqlite3
import datetime


class AlarmDialog(QDialog, AlarmDialog.Ui_Dialog):
    def __init__(self, name='', time='00:00:00', dow='', active=True, to_change=False):
        super().__init__()
        self.setFixedSize(551, 348)
        self.setupUi(self)
        self.setWindowModality(QtCore.Qt.ApplicationModal)

        self.HourBox.setValue(int(time.split(':')[0]))
        self.MinuteBox.setValue(int(time.split(':')[1]))
        self.olds = [name, time, dow, active]
        for i in self.daysOfWeek.children():
            if type(i) != QHBoxLayout:
                if i.text()[:3] in dow:
                    i.setChecked(True)

        if active:
            self.Enabled.setChecked(True)

        self.to_change = to_change

        if not self.to_change:
            self.DeletButton.hide()

        self.DeletButton.clicked.connect(self.delet)

        self.connect = sqlite3.connect("data/AlarmDB.db")
        self.cur = self.connect.cursor()

        self.buttonBox.accepted.connect(self.add_to_db)
        self.buttonBox.rejected.connect(self.cancel)

    def delet(self):
        self.cur.execute(f"""delete from alarm where NameofAlarm = '{self.olds[0]}' and 
Time = '{self.olds[1]}' and 
DaysofWeek = '{self.olds[2]}'""")
        self.connect.commit()
        self.connect.close()
        self.close()




    def add_to_db(self):
        hours = int(self.HourBox.value())
        minutes = int(self.MinuteBox.value())

        time_to_add = datetime.time(hours, minutes)

        days_of_week = ''
        for i in self.daysOfWeek.children():
            if type(i) != QHBoxLayout:
                if i.isChecked():
                    days_of_week += i.text()[0:3] + ' '

        name = self.lineEdit.text()

        enabled = self.Enabled.isChecked()

        if self.to_change:
            if not (self.cur.execute(f"""select * from alarm where NameOfAlarm = '{name}' 
                and daysofweek = '{days_of_week}' and time = '{time_to_add}'""").fetchall()) or \
                    (self.cur.execute(f"""select * from alarm where NameOfAlarm = '{name}' 
                                    and daysofweek = '{days_of_week}' and time = '{time_to_add}'""").fetchall()
                     and enabled != self.olds[3]):
                self.cur.execute(f"""update alarm
    set NameofAlarm = '{name}',
    daysofweek = '{days_of_week}',
    time = '{time_to_add}',
    isactive = {enabled}
    where NameOfAlarm = '{self.olds[0]}' and
    daysofweek = '{self.olds[2]}' and
    time = '{self.olds[1]}'""")


        else:

            if not (self.cur.execute(f"""select * from alarm where NameOfAlarm = '{name}' 
    and daysofweek = '{days_of_week}' and time = '{time_to_add}'""").fetchall()):
                self.cur.execute(f"""insert into 
                    Alarm(NameOfAlarm, Time, daysofweek, isactive) 
                    values('{name}', time('{time_to_add}'), '{days_of_week}', {enabled})""")
        self.connect.commit()
        self.connect.close()

        self.close()

    def cancel(self):
        self.close()
