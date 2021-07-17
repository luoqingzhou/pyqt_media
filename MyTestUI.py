
import sys

from PyQt5 import QtWidgets
from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt5.QtMultimedia import *
from window_practice import Ui_MainWindow


class MyUI(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyUI, self).__init__(parent)
        #  Ui_MainWindow 界面路径
        self.setupUi(self)

        self.is_playing = False
        self.is_selected = False
        self.totalTime = 0
        self.player = QMediaPlayer()
        self.player.setVideoOutput(self.myvideowidget)  # 视频播放输出的widget，就是上面定义的

        self.btnLoad.clicked.connect(self.on_btnLoad_clicked)
        self.btnStart.clicked.connect(self.on_btnStart_clicked)
        self.btnPause.clicked.connect(self.on_btnPause_clicked)
        self.player.positionChanged.connect(self.showCurrentTime)
        self.player.durationChanged.connect(self.showTotalTime)

        print('init finish')

    def on_btnLoad_clicked(self):
        if not self.is_selected:
            self.player.setMedia(QMediaContent(QFileDialog.getOpenFileUrl()[0]))  # 选取视频文件
            self.is_selected = True
            print('load')
            #self.player.play()  # 播放视频
        else:
            pass

    def on_btnStart_clicked(self):
        if not self.is_playing:
            self.player.play()  # 播放视频
            self.is_playing = True
        else:
            pass

    def on_btnPause_clicked(self):
        if self.is_playing:
            self.player.pause()
            self.is_playing = False
        else:
            pass

    def showTotalTime(self):
        # self.timeSlider.setValue(0)
        # self.totalTime = self.player.duration() / 1000
        # self.Slider.setRange(0, int(self.totalTime))
        print(self.player.duration())
        self.timeSlider.setMaximum(self.player.duration())
        print('total')

    def showCurrentTime(self, val):
        # self.timeSlider.setValue(int(val / 1000))
        print(self.player.position())
        self.timeSlider.setValue(val)
        print('current')


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ui = MyUI()
    ui.show()
    sys.exit(app.exec_())