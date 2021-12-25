import os
from designs.ihateit import *
import pygame

CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))


class TimeUp(QtWidgets.QDialog, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.setupUi(self)
        pygame.init()
        self.sound = pygame.mixer.Sound('data/Arthur Morgan Alarm clock.mp3')

        self.sound.play(-1)

        self.pushButton.clicked.connect(self.closee)

    def closee(self):
        self.sound.stop()
        self.close()




# if __name__ == '__main__':
#     print(bool('0'))
#     app = QtWidgets.QApplication(sys.argv)
#     ex = TimeUp()
#     ex.show()
#     sys.exit(app.exec())

# import sys
#

#
# class TimeUp(QtWidgets.QDialog):
#     def __init__(self, music):
#         super().__init__()
#         self.setFixedSize(200, 200)
#         self.lable = QtWidgets.QLabel('Время Вышло!')
#         self.lable.move(97, 100)
#
#         filename = music
#         fullpath = QtCore.QDir.current().absoluteFilePath(filename)
#         url = QtCore.QUrl.fromLocalFile(fullpath)
#         content = QtMultimedia.QMediaContent(url)
#         player = QtMultimedia.QMediaPlayer()
#         player.setMedia(content)
#         player.play()
#
#         self.ok = QtWidgets.QPushButton('ok')
#         self.ok.move(90, 110)
#         self.ok.clicked.connect(self.close)
#
#
# if __name__ == '__main__':
#     app = QtWidgets.QApplication(sys.argv)
#     c = TimeUp('data/asus-yamete-kudasai.mp3')
#     c.show()
#
#
#     sys.exit(app.exec_())
