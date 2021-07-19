
import sys

from PyQt5 import QtWidgets
from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot, QTimer, QRect
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QSlider
from PyQt5.QtMultimedia import *
from window_practice import Ui_MainWindow

from PyQt5 import QtCore, QtGui, QtWidgets


class MyUI(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyUI, self).__init__(parent)
        #  Ui_MainWindow 界面路径
        self.setupUi(self)

        #增加部分ui
        # slider_volume = new
        # CustomSlider(this);
        # slider_volume->setOrientation(Qt::Vertical)
        # slider_volume->setEnabled(false)
        # slider_volume->hide()

        # self.sliderVolume = QSlider(self.frame)
        # self.sliderVolume.setOrientation(QtCore.Qt.Vertical)
        # self.sliderVolume.setEnabled(False)
        # self.sliderVolume.show()

         #
        self.is_playing = False
        self.is_selected = False
        self.is_sliderVolume_show = False
        self.is_finished = False
        self.totalTime = 0

        self.player = QMediaPlayer()
        self.player.setVideoOutput(self.myvideowidget)  # 视频播放输出的widget，就是上面定义的

        self.timer = QTimer()
        self.timer.setInterval(1000);

        self.actionLoad.triggered.connect(self.on_actionLoad_triggered)
        self.actionExit.triggered.connect(self.on_actionExit_triggered)
        
        self.btnStartAndPause.clicked.connect(self.on_btnStartAndPause_clicked)
        
        self.timer.timeout.connect(self.on_timerout)

        self.sliderTime.sliderMoved.connect(self.on_silderTime_moved)
        self.sliderTime.sliderReleased.connect(self.on_silderTime_released)
        self.sliderTime.sliderPressed.connect(self.on_sliderTime_pressed)

        self.sliderVolume.sliderMoved.connect(self.volumeChanged)

        print('init finish')

    def on_actionLoad_triggered(self):
        if not self.is_selected:
            self.player.setMedia(QMediaContent(QFileDialog.getOpenFileUrl()[0]))  # 选取视频文件
            self.is_selected = True
            print('load')
            #self.player.play()  # 播放视频
        else:
            pass

    def on_actionExit_triggered(self):
        sys.exit()

    def on_btnStartAndPause_clicked(self):
        if not self.is_finished:
            if not self.is_playing:
                self.btnStartAndPause.setText('暂停')
                self.player.play()  # 播放视频
                self.timer.start()
                self.is_playing = True
                self.lblVolumeValue.setText(str(self.player.volume()) + '%')
                self.sliderVolume.setValue(self.sliderVolume.maximum())
                self.sliderTime.setMaximum(self.player.duration())
            else:
                self.btnStartAndPause.setText('开始')
                self.player.pause()  # 播放视频
                self.is_playing = False
        else:
            if not self.is_playing:
                self.btnStartAndPause.setText('暂停')
                self.player.play()  # 播放视频
                self.timer.start()
                self.is_playing = True
                self.is_finished = False


    def on_timerout(self):
        print(self.player.position())
        print(self.player.duration())
        self.sliderTimeUpdate()
        self.lblTimeValueUpdate()
        self.finishedTest()

    def on_silderTime_moved(self):
        print('moved')
        self.timer.stop()
        self.player.pause()
        self.player.setPosition(self.sliderTime.value() / self.player.duration() * self.sliderTime.maximum())
        print('moved finished')

    def on_silderTime_released(self):
        print('released')
        self.lblTimeValueUpdate()
        print('update finished')
        self.timer.start()

        self.player.play()
        print('released finished')

    def on_sliderTime_pressed(self, e):
        pass 

    def volumeChanged(self):
        self.player.setVolume(self.sliderVolume.value())
        self.lblVolumeValue.setText(str(self.player.volume()) + '%')

    #时间显示更新
    def lblTimeValueUpdate(self):
        total = int(self.player.duration() / 1000)
        current = int(self.player.position() / 1000)
        totalHour = int(total / 3600)
        totalMin = int(total / 60)
        totalSec = int(total % 60)
        currentHour = int(current / 3600)
        currentMin = int(current / 60)
        currentSec = int(current % 60)
        self.lblTimeValue.setText('{}:{}:{}/{}:{};{}'.format(currentHour, currentMin, currentSec, totalHour, totalMin, totalSec))

    #进度条更新
    def sliderTimeUpdate(self):
        self.sliderTime.setValue(int(self.player.position() / self.player.duration() * self.sliderTime.maximum()))

    def finishedTest(self):
        if self.player.position() == self.player.duration():
            print('finished')
            self.is_finished = True
            self.is_playing = False
            self.btnStartAndPause.setText('重新开始')
            self.timer.stop()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ui = MyUI()
    ui.show()
    sys.exit(app.exec_())