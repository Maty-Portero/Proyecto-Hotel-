# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
##
## Created by: Qt User Interface Compiler version 6.9.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1920, 1080)
        MainWindow.setStyleSheet(u"background-color: rgb(242, 232, 219);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 0, 1920, 1080))
        self.label.setStyleSheet(u"background-color: #F2E8DB;")
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(805, 235, 310, 183))
        self.label_5.setStyleSheet(u"background-color: white;")
        self.label_5.setPixmap(QPixmap(u"../a.png"))
        self.label_5.setScaledContents(True)
        self.pushButton_1 = QPushButton(self.centralwidget)
        self.pushButton_1.setObjectName(u"pushButton_1")
        self.pushButton_1.setGeometry(QRect(847, 765, 227, 76))
        font = QFont()
        font.setFamilies([u"Javanese Text"])
        font.setPointSize(19)
        self.pushButton_1.setFont(font)
        self.pushButton_1.setStyleSheet(u"QPushButton {background-color: white; color: black; border: 2px solid #d0767f; border-radius: 30px; padding: 5px;}\n"
        "QPushButton:hover {background-color: #f0f0f0; border: 2px solid #b3666d;}")
        self.label_15 = QLabel(self.centralwidget)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(0, 1024, 1920, 56))
        font1 = QFont()
        font1.setFamilies([u"Javanese Text"])
        font1.setPointSize(25)
        self.label_15.setFont(font1)
        self.label_15.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_15.setStyleSheet(u"background-color:black;")
        self.label_15.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(680, 187, 561, 705))
        self.label_2.setStyleSheet(u"background-color: white;\n"
"\n"
"\n"
"border: 2px solid white; \n"
"border-radius: 60px; \n"
"padding: 5px;")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(752, 453, 92, 32))
        font2 = QFont()
        font2.setFamilies([u"Javanese Text"])
        font2.setPointSize(20)
        self.label_3.setFont(font2)
        self.label_3.setStyleSheet(u"background-color: white;\n"
"color:black;")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(751, 613, 142, 32))
        self.label_4.setFont(font2)
        self.label_4.setStyleSheet(u"background-color: white;\n"
"color:black;")
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(752, 496, 416, 76))
        font3 = QFont()
        font3.setFamilies([u"Javanese Text"])
        font3.setPointSize(15)
        self.lineEdit.setFont(font3)
        self.lineEdit.setStyleSheet(u"background-color: white;\n"
"color: black;\n"
"\n"
"border: 2px solid black; \n"
"border-radius: 20px; \n"
"padding: 5px;")
        self.lineEdit_2 = QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(752, 656, 416, 76))
        self.lineEdit_2.setFont(font3)
        self.lineEdit_2.setStyleSheet(u"background-color: white;\n"
"color: black;\n"
"\n"
"border: 2px solid black; \n"
"border-radius: 20px; \n"
"padding: 5px;")
        MainWindow.setCentralWidget(self.centralwidget)
        self.label.raise_()
        self.label_15.raise_()
        self.label_2.raise_()
        self.label_5.raise_()
        self.pushButton_1.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.lineEdit.raise_()
        self.lineEdit_2.raise_()

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText("")
        self.label_5.setText("")
        self.pushButton_1.setText(QCoreApplication.translate("MainWindow", u"Ingresar", None))
        self.label_15.setText("")
        self.label_2.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Usuario", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Contrase\u00f1a", None))
    # retranslateUi

