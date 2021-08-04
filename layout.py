from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QObject, QThread, pyqtSignal
from time import sleep

a=0
m=1
c=10
c2=10
at=1

#step 1 worker class
class Worker(QObject):
    finished = pyqtSignal()
    progress = pyqtSignal(int)

    def run(self):
        global at
        global a
        """Long-running task."""
        #for i in range(50):
        while True:
            sleep(1)
            a+=at
            self.progress.emit(a)
        self.finished.emit()


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(804, 265)
        MainWindow.setStyleSheet("font: 8pt \"Acumin Pro\";")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.button1 = QtWidgets.QPushButton(self.centralwidget)
        self.button1.setGeometry(QtCore.QRect(50, 200, 75, 23))
        self.button1.setObjectName("button1")
        self.label1 = QtWidgets.QLabel(self.centralwidget)
        self.label1.setGeometry(QtCore.QRect(50, 30, 1461, 31))
        self.label1.setStyleSheet("color: rgb(255, 255, 255);\n"
"text-decoration: underline;\n"
"font: 18pt \"MS Shell Dlg 2\";")
        self.label1.setObjectName("label1")
        self.button2 = QtWidgets.QPushButton(self.centralwidget)
        self.button2.setGeometry(QtCore.QRect(170, 200, 75, 23))
        self.button2.setObjectName("button2")
        self.label1_2 = QtWidgets.QLabel(self.centralwidget)
        self.label1_2.setGeometry(QtCore.QRect(50, 90, 1461, 31))
        self.label1_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"text-decoration: underline;\n"
"font: 18pt \"MS Shell Dlg 2\";")
        self.label1_2.setObjectName("label1_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 10, 47, 13))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(50, 70, 71, 16))
        self.label_2.setObjectName("label_2")
        self.startclicker = QtWidgets.QPushButton(self.centralwidget)
        self.startclicker.setGeometry(QtCore.QRect(280, 200, 121, 23))
        self.startclicker.setObjectName("startclicker")
        self.upgradeclicker = QtWidgets.QPushButton(self.centralwidget)
        self.upgradeclicker.setGeometry(QtCore.QRect(430, 200, 151, 23))
        self.upgradeclicker.setObjectName("upgradeclicker")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(50, 130, 131, 16))
        self.label_3.setObjectName("label_3")
        self.label1_3 = QtWidgets.QLabel(self.centralwidget)
        self.label1_3.setGeometry(QtCore.QRect(50, 150, 1461, 31))
        self.label1_3.setStyleSheet("color: rgb(255, 255, 255);\n"
"text-decoration: underline;\n"
"font: 18pt \"MS Shell Dlg 2\";")
        self.label1_3.setObjectName("label1_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 804, 20))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.button1.setText(_translate("MainWindow", "CLICK"))
        self.label1.setText(_translate("MainWindow", str(a)))
        self.button2.setText(_translate("MainWindow", "UPGRADE"))
        self.label1_2.setText(_translate("MainWindow", str(c)))
        self.label.setText(_translate("MainWindow", "Money"))
        self.label_2.setText(_translate("MainWindow", "Upgrade cost"))
        self.startclicker.setText(_translate("MainWindow", "START AUTOCLICKER"))
        self.upgradeclicker.setText(_translate("MainWindow", "UPGRADE AUTOCLICKER"))
        self.label_3.setText(_translate("MainWindow", "Autoclicker upgrade cost"))
        self.label1_3.setText(_translate("MainWindow", str(c2)))
#############################################################################################################
        self.button1.clicked.connect(self.button_clicked)
        self.button2.clicked.connect(self.upgrade_clicked)
        self.startclicker.clicked.connect(self.autoclicker_clicked)
        self.upgradeclicker.clicked.connect(self.upgrade_clicker)
        '''
        if c>a:
            self.button2.setEnabled(False)
        else:
            self.button2.setEnabled(True)
        '''

    def button_clicked(self):
        global a
        global m
        a=a+(1*m)
        self.label1.setText(str(a))
        '''
        if c>a:
            self.button2.setEnabled(False)
            self.upgradeclicker.setEnabled(False)
        else:
            self.button2.setEnabled(True)
            self.upgradeclicker.setEnabled(True)
        '''

    def upgrade_clicked(self):
        global m
        global c
        global a
        if a>=c:
            a=a-c
            m=m*2
            c=c*2
        else:
            pass
        self.label1_2.setText(str(c))
        self.label1.setText(str(a))

    def reportProgress(self,a):
        #global a
        self.label1.setText(str(a))

    def upgrade_clicker(self):
        global a
        global c2
        global at
        if a>=c2:
            a=a-c2
            at=at*2
            c2=c2*2
        else:
            pass
        self.label1_3.setText(str(c2))
        self.label1.setText(str(a))


    def autoclicker_clicked(self):

        global a
        global c
        self.label1_2.setText(str(c))
        self.label1.setText(str(a))
        # Step 2: Create a QThread object
        self.thread = QThread()
        # Step 3: Create a worker object
        self.worker = Worker()
        # Step 4: Move worker to the thread
        self.worker.moveToThread(self.thread)
        # Step 5: Connect signals and slots
        self.thread.started.connect(self.worker.run)
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)
        self.worker.progress.connect(self.reportProgress)
        # Step 6: Start the thread
        self.thread.start()

        self.startclicker.setEnabled(False)
        # Final resets
        '''
        self.longRunningBtn.setEnabled(False)
        self.thread.finished.connect(
            lambda: self.longRunningBtn.setEnabled(True)
        )

        self.thread.finished.connect(
            lambda: self.label1.setText("Long-Running Step: 0")
        )
        '''


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
