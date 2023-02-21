from PyQt6.QtWidgets import QMainWindow, QLabel, QPushButton, QLineEdit, QHBoxLayout, QVBoxLayout, QCheckBox, QMessageBox, QApplication, QWidget
from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(434, 447)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(170, 40, 91, 91))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../profile.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.lineEdit_5 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(210, 170, 113, 20))
        self.lineEdit_5.setStyleSheet("border-radius:10px;\n"
                                      "border:1px solid green")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.layoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(170, 300, 96, 43))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_3 = QtWidgets.QPushButton(parent=self.layoutWidget)
        self.pushButton_3.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../google.png"),
                       QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_3.setIcon(icon)
        self.pushButton_3.setIconSize(QtCore.QSize(35, 35))
        self.pushButton_3.setCheckable(False)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.pushButton_4 = QtWidgets.QPushButton(parent=self.layoutWidget)
        self.pushButton_4.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../facebook.png"),
                        QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_4.setIcon(icon1)
        self.pushButton_4.setIconSize(QtCore.QSize(35, 35))
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout.addWidget(self.pushButton_4)
        self.pushButton_5 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(260, 370, 71, 21))
        self.pushButton_5.setObjectName("pushstyle_5")
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_5.setFont(font)
        style_5 ="""
        #pushstyle_5{
                color:white;
                background-color: black;
                border-radius:10px;
                font: 14pt \"Microsoft YaHei UI\";
        }
        #pushstyle_5::hover{
                color:red;
        }
        """
        self.pushButton_5.setStyleSheet(style_5)
        
        # self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.clicked.connect(self.quit)

        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(140, 170, 111, 16))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.label_3.setWordWrap(False)
        self.label_3.setOpenExternalLinks(False)
        self.label_3.setObjectName("label_3")

        self.pushButton_6 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_6.setObjectName("pushButton_f")

        self.pushButton_6.setGeometry(QtCore.QRect(120, 370, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_6.setFont(font)
        style = """
        #pushButton_f{
                color: white;
                background-color:black;
                border-radius:10px;
                font: 14pt \"Microsoft YaHei UI\";
        }
        #pushButton_f::hover{
        color:red;
        }
        """
        self.pushButton_6.setStyleSheet(style)
        # self.pushButton_6.setObjectName("pushButton_6")
        self.lineEdit_3 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(210, 250, 113, 20))
        self.lineEdit_3.setStyleSheet("border-radius:10px;\n"
                                      "border:1px solid green")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(120, 250, 81, 20))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(210, 210, 113, 20))
        self.lineEdit_2.setStyleSheet("border-radius:10px;\n"
                                      "border:1px solid green;\n")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3.setEchoMode(QLineEdit().echoMode().Password)
        self.label_5 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(120, 210, 61, 20))
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(140, 210, 81, 20))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 434, 18))
        self.menubar.setObjectName("menubar")
        self.menuro_yhatdan_o_tish = QtWidgets.QMenu(parent=self.menubar)
        self.menuro_yhatdan_o_tish.setObjectName("menuro_yhatdan_o_tish")
        self.menukirish = QtWidgets.QMenu(parent=self.menubar)
        self.menukirish.setObjectName("menukirish")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionabout = QtGui.QAction(parent=MainWindow)
        self.actionabout.setObjectName("actionabout")
        self.actionhome = QtGui.QAction(parent=MainWindow)
        self.actionhome.setObjectName("actionhome")
        self.menuro_yhatdan_o_tish.addAction(self.actionabout)
        self.menukirish.addAction(self.actionhome)
        self.menubar.addAction(self.menuro_yhatdan_o_tish.menuAction())
        self.menubar.addAction(self.menukirish.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_5.setText(_translate("MainWindow", "EXIT"))
        self.label_3.setText(_translate("MainWindow", "name : "))
        self.pushButton_6.setText(_translate("MainWindow", "Back"))
        self.label_4.setText(_translate("MainWindow", "password :"))
        self.label_6.setText(_translate("MainWindow", "email : "))
        self.menuro_yhatdan_o_tish.setTitle(
            _translate("MainWindow", "ro\'yhatdan o\'tish"))
        self.menukirish.setTitle(_translate("MainWindow", "kirish"))
        self.actionabout.setText(_translate("MainWindow", "about"))
        self.actionhome.setText(_translate("MainWindow", "home"))
 
    def quit(self):
        QtWidgets.QApplication.quit() 

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
