# pyqt_media

### 环境及其配置
python版本：3.75

第三方库：

PyQt5   5.15.4

开发环境：

PyCharm professional 2021.1.1

QtDesigner 5.14.2

### 源文件代码解释
window_practice.ui 为QtDesigner文件

window_practice.py 为ui文件对应生成的py文件

MyTestUI.py 为继承window_practice.py 的py文件，主要进行功能的实现

mySlier.py 为继承增加功能的slider，主要功能为实现进度条的点击、拖动

myVedioWight.py 为继承videoWight，主要功能实现点击视频暂停

其他3个video开头的文件为网上的参考代码，其UI还可以（使用QSS）和主工程无关

### 其他问题

#### 如何使用
1. 运行MyTestUI文件
2. 开始菜单中可以加载MP4文件，点击播放即可

#### 视频无法播放
应该是缺少mp4编码器，百度搜索pyqt、mp4编码器即可

#### 如何ui生成py
百度搜索pyqt、pyuic关键词即可
