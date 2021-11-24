from stopwatch import *
import Alarm
from designs.timesettter import Ui_MainWindow
from designs.setter import Ui_Dialog
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.value = ''
        self.timeset.clicked.connect(self.get_value)
        self.alarm = Alarm.Alarm()


    def get_value(self):
        dialog = InputDialog(self)
        # this will show the dialog and wait for the user to accept or reject it
        if dialog.exec():
            # get the value from the dialog
            value, name = dialog.getValue()
            self.add_to_db(value, name)
            self.initiate_alarm()

    def add_to_db(self, value, name):
        cursor.execute(f"""insert into alarm (NameofAlarm, DateAndTime) values
        ('{name}', '{value}')""")
        cursor.execute("""select * from Alarm order by datetime(DateAndTime)""")
        dbconnect.commit()

    def initiate_alarm(self):
        self.alarm.start()
        self.alarm.join()


class InputDialog(QtWidgets.QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

    def getValue(self):
        # return the current value of the spinbox
        return self.date_and_time.text(), self.name.text()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec())