import datetime
import HandleDate
import sqlite3
import threading
import time
from stopwatch import *


class Alarm:
    def __init__(self):
        self.thread = threading.Thread(target=self.check_for_time)
        self.flag = False

    def get_time(self):
        if cursor.execute("""select * from alarm where
                     not(nameofalarm = 'dummy') """).fetchall():
            self.id = cursor.execute("""select * from Alarm where not(nameofalarm = 'dummy') """).fetchone()[0]
            self.time = cursor.execute("""select * from Alarm where not(nameofalarm = 'dummy') """).fetchone()[2]
            self.name = cursor.execute("""select * from Alarm where not(nameofalarm = 'dummy') """).fetchone()[1]
            self.time = datetime.datetime.strptime(self.time, '%Y-%m-%d %H:%M:%S')
            print(self.time, type(self.time))
            self.check_for_time()
        else:
            self.flag = False
            self.time, self.name, self.id = None, None, None

    def start(self):
        self.thread.start()

    def join(self):
        self.thread.join()

    def check_for_time(self):
        self.get_time()
        self.flag = False
        while True:
            if self.time and datetime.datetime.now() >= self.time:
                print(f'ПОЗДРАВЛЯЮ {self.name}')

                time.sleep(.5)
                self.flag = True
                cursor.execute(f"""delete from alarm where id={self.id}""")
                dbconnect.commit()

            if self.flag:
                self.get_time()
            else:
                self.flag = False
                self.id = None
                self.time = None
                self.name = None
            # elif flag and not (self.cursor.execute("""select * from alarm where
            #  not(nameofalarm = 'dummy') """).fetchall()):
            #     break

