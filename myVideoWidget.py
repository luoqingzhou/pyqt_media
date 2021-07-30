from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtCore import *
class myVideoWidget(QVideoWidget):
    screenPressed = pyqtSignal()  # 创建双击信号

    def __init__(self,parent=None):
        super(QVideoWidget,self).__init__(parent)

    def mousePressEvent(self, QMouseEvent):     #双击事件
        print('screen clicked')
        self.screenPressed.emit()

