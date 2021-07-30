from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys


class mySlider(QtWidgets.QSlider):
    mySliderPressed = pyqtSignal()

    def __init__(self, parent=None):
        super(mySlider, self).__init__(parent)

    def mousePressEvent(self, event):
        # / 注意应先调用父类的鼠标点击处理事件，这样可以不影响拖动的情况
        # QSlider::mousePressEvent(ev);
        # // 获取鼠标的位置，这里并不能直接从ev中取值（因为如果是拖动的话，鼠标开始点击的位置没有意义了）
        # double
        # pos = ev->pos().x() / (double)
        # width();
        # setValue(pos * (maximum() - minimum()) + minimum());
        # // 发送自定义的鼠标单击信号
        # emit
        # costomSliderClicked();
        print('slider pressed')
        if event.buttons() == QtCore.Qt.LeftButton:
            print('left')
            self.setSliderPosition(event.pos().x() / self.width() * self.maximum())
            print(event.pos().x())
        self.mySliderPressed.emit()

