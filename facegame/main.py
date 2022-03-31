import sys,os,cv2,random,numpy as np
from datetime import datetime
# 导入图形组件库
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtMultimedia import *
#导入做好的界面库
from untitled import Ui_MainWindow

class MainWindow(QMainWindow,Ui_MainWindow):
    def __init__(self):
        #继承(QMainWindow,Ui_MainWindow)父类的属性
        super(MainWindow,self).__init__()
        # 初始化界面组件
        self.setupUi(self)

        self.label_11.setPixmap(QPixmap(r"static\no_signal.jpg").scaled(677,647))
        self.label_11.setScaledContents(True)
        self.label_14.setScaledContents(True)
        self.label_3.setScaledContents(True)
        self.label_2.setScaledContents(True)

        #初始化页数设置
        self.stackedWidget.setCurrentIndex(0)
        #设置定时器
        self.time = QTimer()
        self.time.timeout.connect(self.refrsh)

        self.time1 = QTimer()
        self.time1.timeout.connect(self.refrsh1)
        #开始
        self.pushButton.clicked.connect(self.startMain)
        #单人模式
        self.pushButton_6.clicked.connect(lambda :self.stackedWidget.setCurrentIndex(2))
        #多人模式
        self.pushButton_5.clicked.connect(self.getCamra1)

        # 单人模式
        # level 1
        self.pushButton_2.clicked.connect(self.getNum1)
        # level 2
        self.pushButton_3.clicked.connect(self.getNum2)
        # level 3
        self.pushButton_4.clicked.connect(self.getNum3)
        self.status = None  # 判断状态
        self.cap = None
        self.cap1 = None
        # 暂停音乐
        self.pushButton_17.clicked.connect(self.stopMusic)
        # 播放音乐
        self.pushButton_9.clicked.connect(self.startMusic)
        # 重玩
        self.pushButton_10.clicked.connect(self.backMain)
        # 结束游戏
        self.pushButton_11.clicked.connect(self.overGame1)
        self.verticalSlider.valueChanged.connect(self.valChange)




        #多人模式
        self.status1 = None#判断状态
        self.cap = None
        self.cap1 = None
        #暂停音乐
        self.pushButton_18.clicked.connect(self.stopMusic1)
        #播放音乐
        self.pushButton_14.clicked.connect(self.startMusic1)
        #重玩
        self.pushButton_15.clicked.connect(self.backMain)
        #结束游戏
        self.pushButton_16.clicked.connect(self.overGame1)
        self.verticalSlider_2.valueChanged.connect(self.valChange1)

        #返回主界面
        self.pushButton_12.clicked.connect(lambda :self.stackedWidget.setCurrentIndex(0))
        #结束
        self.pushButton_13.clicked.connect(self.close)
    ####识别的api接口
    def getResult(self):
        return True


    def stopMusic1(self):
        self.media_player.pause()

    def startMusic1(self):
        self.media_player.play()

    def valChange1(self):
        self.label_13.setNum(self.verticalSlider_2.value())  # 注意这里别setText 会卡死

    def startMain(self):

        # 单人模式初始化
        self.label.clear()
        self.label_6.clear()
        self.label_7.clear()
        self.verticalSlider_2.setValue(0)

        #多人模式初始化
        self.label_13.clear()
        self.label_16.clear()
        self.label_18.clear()
        self.verticalSlider_2.setValue(0)



        #分数
        self.score = 0

        self.media_player = QMediaPlayer(self)
        self.stackedWidget.setCurrentIndex(1)
    def backMain(self):
        self.media_player.stop()
        self.stackedWidget.setCurrentIndex(0)
    def overGame1(self):
        if self.time1.isActive():
            self.time1.stop()
            self.cap.release()
            self.cap1.release()
        self.media_player.stop()
        self.stackedWidget.setCurrentIndex(5)
        self.label_8.setText(f"分数：{self.score}")

    def getCamra1(self):
        #切换
        self.stackedWidget.setCurrentIndex(4)
        abs_path = os.path.abspath(r"static\music\background.mp3")
        url = QUrl.fromLocalFile(abs_path)
        c = QMediaContent(url)
        self.media_player.setMedia(c)
        self.media_player.play()

        if self.time1.isActive():
            self.cap.release()
            self.cap1.release()
            self.time1.stop()

        self.cap = cv2.VideoCapture(0)
        try:
            self.cap1 = cv2.VideoCapture(1)
        except:
            self.label_11.setPixmap(QPixmap(r"static\no_signal.jpg").scaled(677,647))
        self.localTimeDouble = datetime.now()
        #0 就是左边的可以动  1 不可以
        self.status1 = 0
        self.time1.start()

    def refrsh1(self):
        if self.status1 == 0:
            now = datetime.now()
            dateGet = (now - self.localTimeDouble).seconds
            self.label_16.setText(str(30-dateGet))
            if dateGet == 30:
                self.status1 = 1

            #第一玩家
            ref, frame = self.cap.read()
            if ref:

                # 格式转变，BGRtoRGB
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                # 进行检测
                r_image = np.array(frame)
                showImage = QImage(r_image, r_image.shape[1], r_image.shape[0], 3 * r_image.shape[1], QImage.Format_RGB888).scaled(677,647)
                self.label_14.setPixmap(QPixmap.fromImage(showImage))
            try:
                ref1, frame1 = self.cap1.read()
                if ref1:
                    # 格式转变，BGRtoRGB
                    frame = cv2.cvtColor(frame1, cv2.COLOR_BGR2RGB)
                    # 进行检测
                    r_image = np.array(frame)
                    showImage = QImage(r_image, r_image.shape[1], r_image.shape[0], 3 * r_image.shape[1], QImage.Format_RGB888).scaled(677,647)
                    self.label_11.setPixmap(QPixmap.fromImage(showImage))
            except:
                pass
        elif self.status1 == 1:
            now = datetime.now()
            dateGet = (now - self.localTimeDouble).seconds
            self.label_16.setText(str(30 - dateGet))
            if self.getResult():
                self.status1 = 0
                self.score = int(self.label_18.text()) + 1
                #分数
                self.label_18.setText(str(int(self.label_18.text()) + 1))
                #相似度
                self.verticalSlider_2.setValue(80)
                self.localTimeDouble = now
            # 第一玩家
            ref, frame = self.cap.read()
            if ref:
                # 格式转变，BGRtoRGB
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                # 进行检测
                r_image = np.array(frame)
                showImage = QImage(r_image, r_image.shape[1], r_image.shape[0], 3 * r_image.shape[1],
                                   QImage.Format_RGB888).scaled(677, 647)
                self.label_14.setPixmap(QPixmap.fromImage(showImage))
    #单人模式
    def stopMusic(self):
        self.media_player.pause()

    def startMusic(self):
        self.media_player.play()

    def valChange(self):
        self.label_7.setNum(self.verticalSlider.value())  # 注意这里别setText 会卡死

    def getNum1(self):
        abs_path = os.path.abspath(r"static\music\background.mp3")
        url = QUrl.fromLocalFile(abs_path)
        c = QMediaContent(url)
        self.media_player.setMedia(c)
        self.media_player.play()
        self.data = []
        path = "img"
        for i in os.listdir(path):
            self.data.append(os.path.join(path,i))
        self.resetTime = 10
        self.picTotal = 14
        self.index = 0
        self.stackedWidget.setCurrentIndex(3)
        if self.time.isActive():
            self.cap.release()
            self.time.stop()
        self.localTimeDouble = datetime.now()
        self.cap = cv2.VideoCapture(0)
        self.label_3.setPixmap(QPixmap(random.choice(self.data)).scaled(677,647))
        self.time.start()
    def getNum2(self):
        abs_path = os.path.abspath(r"static\music\background.mp3")
        url = QUrl.fromLocalFile(abs_path)
        c = QMediaContent(url)
        self.media_player.setMedia(c)
        self.media_player.play()
        self.data = []
        path = "img"
        for i in os.listdir(path):
            self.data.append(os.path.join(path, i))
        self.resetTime = 7
        self.picTotal = 14
        self.index = 0
        self.stackedWidget.setCurrentIndex(3)
        if self.time.isActive():
            self.cap.release()
            self.time.stop()
        self.localTimeDouble = datetime.now()
        self.cap = cv2.VideoCapture(0)
        self.label_3.setPixmap(QPixmap(random.choice(self.data)).scaled(677, 647))
        self.time.start()
    def getNum3(self):
        abs_path = os.path.abspath(r"static\music\background.mp3")
        url = QUrl.fromLocalFile(abs_path)
        c = QMediaContent(url)
        self.media_player.setMedia(c)
        self.media_player.play()
        self.data = []
        path = "img"
        for i in os.listdir(path):
            self.data.append(os.path.join(path, i))
        #设置时间
        self.resetTime = 3
        #图片数量
        self.picTotal = 14
        self.index = 0
        self.stackedWidget.setCurrentIndex(3)
        if self.time.isActive():
            self.cap.release()
            self.time.stop()
        self.localTimeDouble = datetime.now()
        self.cap = cv2.VideoCapture(0)
        self.label_3.setPixmap(QPixmap(random.choice(self.data)).scaled(677, 647))
        self.time.start()
    def refrsh(self):
        ref, frame = self.cap.read()
        if ref:
            now = datetime.now()
            dateGet = (now - self.localTimeDouble).seconds
            self.label.setText(str(self.resetTime - dateGet))
            if dateGet == self.resetTime:
                self.index += 1
                if self.index == self.picTotal:
                    self.time.stop()
                    self.cap.release()
                    self.media_player.stop()
                    self.stackedWidget.setCurrentIndex(5)
                    self.label_8.setText(f"分数：{self.score}")
                self.localTimeDouble = now
                self.label_3.setPixmap(QPixmap(random.choice(self.data)).scaled(677, 647))
            if self.getResult():
                num = 1#奖励
                self.score += num
                self.label_6.setText(str(self.score))
                #相似度
                self.verticalSlider.setValue(50)
            # 格式转变，BGRtoRGB
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            # 进行检测
            r_image = np.array(frame)
            showImage = QImage(r_image, r_image.shape[1], r_image.shape[0], 3 * r_image.shape[1], QImage.Format_RGB888).scaled(584,345)
            self.label_2.setPixmap(QPixmap.fromImage(showImage))


    def closeEvent(self, a0: QCloseEvent) -> None:
        if self.time.isActive():
            self.cap.release()
            self.time.stop()
if __name__ == "__main__":
    #创建QApplication 固定写法
    app = QApplication(sys.argv)
    # import ctypes
    # ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("myappid")
    # 实例化界面
    window = MainWindow()
    #显示界面
    window.show()
    #阻塞，固定写法
    sys.exit(app.exec_())