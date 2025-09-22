# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'eleccion_habitacion.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QMainWindow,
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
        self.label_5.setGeometry(QRect(842, 63, 237, 158))
        self.label_5.setStyleSheet(u"background-color: rgb(242, 232, 219);")
        self.label_5.setPixmap(QPixmap(u"../c.png"))
        self.label_5.setScaledContents(True)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(890, 260, 295, 39))
        font = QFont()
        font.setFamilies([u"Javanese Text"])
        font.setPointSize(25)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"color:black;")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(476, 340, 274, 47))
        font1 = QFont()
        font1.setFamilies([u"Javanese Text"])
        font1.setPointSize(30)
        self.label_4.setFont(font1)
        self.label_4.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_4.setStyleSheet(u"color:black;")
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(82, 318, 1068, 10))
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)
        self.line_2 = QFrame(self.centralwidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(77, 394, 1068, 10))
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(137, 430, 15, 39))
        self.label_6.setFont(font)
        self.label_6.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_6.setStyleSheet(u"color:black;")
        self.label_6.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(290, 430, 23, 39))
        self.label_7.setFont(font)
        self.label_7.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_7.setStyleSheet(u"color:black;")
        self.label_7.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(450, 430, 18, 39))
        self.label_8.setFont(font)
        self.label_8.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_8.setStyleSheet(u"color:black;")
        self.label_8.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(611, 431, 7, 39))
        self.label_9.setFont(font)
        self.label_9.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_9.setStyleSheet(u"color:black;")
        self.label_9.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_10 = QLabel(self.centralwidget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(765, 430, 18, 39))
        self.label_10.setFont(font)
        self.label_10.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_10.setStyleSheet(u"color:black;")
        self.label_10.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_11 = QLabel(self.centralwidget)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(1072, 430, 23, 39))
        self.label_11.setFont(font)
        self.label_11.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_11.setStyleSheet(u"color:black;")
        self.label_11.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_12 = QLabel(self.centralwidget)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(919, 430, 16, 39))
        self.label_12.setFont(font)
        self.label_12.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_12.setStyleSheet(u"color:black;")
        self.label_12.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.line_3 = QFrame(self.centralwidget)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setGeometry(QRect(77, 475, 1068, 10))
        self.line_3.setFrameShape(QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)
        self.pushButton_1 = QPushButton(self.centralwidget)
        self.pushButton_1.setObjectName(u"pushButton_1")
        self.pushButton_1.setGeometry(QRect(80, 488, 125, 70))
        font2 = QFont()
        font2.setFamilies([u"Javanese Text"])
        font2.setPointSize(19)
        self.pushButton_1.setFont(font2)
        self.pushButton_1.setStyleSheet(u"background-color: WHITE;\n"
"color: black;\n"
"\n"
"border: 2px solid #d0767f; \n"
"border-radius: 30px; \n"
"padding: 5px;")
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(240, 488, 125, 70))
        self.pushButton_2.setFont(font2)
        self.pushButton_2.setStyleSheet(u"background-color: WHITE;\n"
"color: black;\n"
"\n"
"border: 2px solid #d0767f; \n"
"border-radius: 30px; \n"
"padding: 5px;")
        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(550, 490, 125, 70))
        self.pushButton_3.setFont(font2)
        self.pushButton_3.setStyleSheet(u"background-color: WHITE;\n"
"color: black;\n"
"\n"
"border: 2px solid #d0767f; \n"
"border-radius: 30px; \n"
"padding: 5px;")
        self.pushButton_4 = QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(710, 490, 125, 70))
        self.pushButton_4.setFont(font2)
        self.pushButton_4.setStyleSheet(u"background-color: WHITE;\n"
"color: black;\n"
"\n"
"border: 2px solid #d0767f; \n"
"border-radius: 30px; \n"
"padding: 5px;")
        self.pushButton_5 = QPushButton(self.centralwidget)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(860, 490, 125, 70))
        self.pushButton_5.setFont(font2)
        self.pushButton_5.setStyleSheet(u"background-color: WHITE;\n"
"color: black;\n"
"\n"
"border: 2px solid #d0767f; \n"
"border-radius: 30px; \n"
"padding: 5px;")
        self.pushButton_6 = QPushButton(self.centralwidget)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setGeometry(QRect(1020, 490, 125, 70))
        self.pushButton_6.setFont(font2)
        self.pushButton_6.setStyleSheet(u"background-color: WHITE;\n"
"color: black;\n"
"\n"
"border: 2px solid #d0767f; \n"
"border-radius: 30px; \n"
"padding: 5px;")
        self.pushButton_7 = QPushButton(self.centralwidget)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setGeometry(QRect(390, 490, 125, 70))
        self.pushButton_7.setFont(font2)
        self.pushButton_7.setStyleSheet(u"background-color: WHITE;\n"
"color: black;\n"
"\n"
"border: 2px solid #d0767f; \n"
"border-radius: 30px; \n"
"padding: 5px;")
        self.pushButton_8 = QPushButton(self.centralwidget)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setGeometry(QRect(860, 570, 125, 70))
        self.pushButton_8.setFont(font2)
        self.pushButton_8.setStyleSheet(u"background-color: WHITE;\n"
"color: black;\n"
"\n"
"border: 2px solid #d0767f; \n"
"border-radius: 30px; \n"
"padding: 5px;")
        self.pushButton_9 = QPushButton(self.centralwidget)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setGeometry(QRect(80, 570, 125, 70))
        self.pushButton_9.setFont(font2)
        self.pushButton_9.setStyleSheet(u"background-color: WHITE;\n"
"color: black;\n"
"\n"
"border: 2px solid #d0767f; \n"
"border-radius: 30px; \n"
"padding: 5px;")
        self.pushButton_10 = QPushButton(self.centralwidget)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setGeometry(QRect(550, 570, 125, 70))
        self.pushButton_10.setFont(font2)
        self.pushButton_10.setStyleSheet(u"background-color: WHITE;\n"
"color: black;\n"
"\n"
"border: 2px solid #d0767f; \n"
"border-radius: 30px; \n"
"padding: 5px;")
        self.pushButton_11 = QPushButton(self.centralwidget)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setGeometry(QRect(390, 570, 125, 70))
        self.pushButton_11.setFont(font2)
        self.pushButton_11.setStyleSheet(u"background-color: WHITE;\n"
"color: black;\n"
"\n"
"border: 2px solid #d0767f; \n"
"border-radius: 30px; \n"
"padding: 5px;")
        self.pushButton_12 = QPushButton(self.centralwidget)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setGeometry(QRect(1020, 570, 125, 70))
        self.pushButton_12.setFont(font2)
        self.pushButton_12.setStyleSheet(u"background-color: WHITE;\n"
"color: black;\n"
"\n"
"border: 2px solid #d0767f; \n"
"border-radius: 30px; \n"
"padding: 5px;")
        self.pushButton_13 = QPushButton(self.centralwidget)
        self.pushButton_13.setObjectName(u"pushButton_13")
        self.pushButton_13.setGeometry(QRect(240, 570, 125, 70))
        self.pushButton_13.setFont(font2)
        self.pushButton_13.setStyleSheet(u"background-color: WHITE;\n"
"color: black;\n"
"\n"
"border: 2px solid #d0767f; \n"
"border-radius: 30px; \n"
"padding: 5px;")
        self.pushButton_14 = QPushButton(self.centralwidget)
        self.pushButton_14.setObjectName(u"pushButton_14")
        self.pushButton_14.setGeometry(QRect(710, 570, 125, 70))
        self.pushButton_14.setFont(font2)
        self.pushButton_14.setStyleSheet(u"background-color: WHITE;\n"
"color: black;\n"
"\n"
"border: 2px solid #d0767f; \n"
"border-radius: 30px; \n"
"padding: 5px;")
        self.pushButton_15 = QPushButton(self.centralwidget)
        self.pushButton_15.setObjectName(u"pushButton_15")
        self.pushButton_15.setGeometry(QRect(860, 650, 125, 70))
        self.pushButton_15.setFont(font2)
        self.pushButton_15.setStyleSheet(u"background-color: WHITE;\n"
"color: black;\n"
"\n"
"border: 2px solid #d0767f; \n"
"border-radius: 30px; \n"
"padding: 5px;")
        self.pushButton_16 = QPushButton(self.centralwidget)
        self.pushButton_16.setObjectName(u"pushButton_16")
        self.pushButton_16.setGeometry(QRect(80, 730, 125, 70))
        self.pushButton_16.setFont(font2)
        self.pushButton_16.setStyleSheet(u"background-color: WHITE;\n"
"color: black;\n"
"\n"
"border: 2px solid #d0767f; \n"
"border-radius: 30px; \n"
"padding: 5px;")
        self.pushButton_17 = QPushButton(self.centralwidget)
        self.pushButton_17.setObjectName(u"pushButton_17")
        self.pushButton_17.setGeometry(QRect(390, 730, 125, 70))
        self.pushButton_17.setFont(font2)
        self.pushButton_17.setStyleSheet(u"background-color: WHITE;\n"
"color: black;\n"
"\n"
"border: 2px solid #d0767f; \n"
"border-radius: 30px; \n"
"padding: 5px;")
        self.pushButton_18 = QPushButton(self.centralwidget)
        self.pushButton_18.setObjectName(u"pushButton_18")
        self.pushButton_18.setGeometry(QRect(550, 730, 125, 70))
        self.pushButton_18.setFont(font2)
        self.pushButton_18.setStyleSheet(u"background-color: WHITE;\n"
"color: black;\n"
"\n"
"border: 2px solid #d0767f; \n"
"border-radius: 30px; \n"
"padding: 5px;")
        self.pushButton_19 = QPushButton(self.centralwidget)
        self.pushButton_19.setObjectName(u"pushButton_19")
        self.pushButton_19.setGeometry(QRect(80, 650, 125, 70))
        self.pushButton_19.setFont(font2)
        self.pushButton_19.setStyleSheet(u"background-color: WHITE;\n"
"color: black;\n"
"\n"
"border: 2px solid #d0767f; \n"
"border-radius: 30px; \n"
"padding: 5px;")
        self.pushButton_20 = QPushButton(self.centralwidget)
        self.pushButton_20.setObjectName(u"pushButton_20")
        self.pushButton_20.setGeometry(QRect(550, 650, 125, 70))
        self.pushButton_20.setFont(font2)
        self.pushButton_20.setStyleSheet(u"background-color: WHITE;\n"
"color: black;\n"
"\n"
"border: 2px solid #d0767f; \n"
"border-radius: 30px; \n"
"padding: 5px;")
        self.pushButton_21 = QPushButton(self.centralwidget)
        self.pushButton_21.setObjectName(u"pushButton_21")
        self.pushButton_21.setGeometry(QRect(390, 650, 125, 70))
        self.pushButton_21.setFont(font2)
        self.pushButton_21.setStyleSheet(u"background-color: WHITE;\n"
"color: black;\n"
"\n"
"border: 2px solid #d0767f; \n"
"border-radius: 30px; \n"
"padding: 5px;")
        self.pushButton_22 = QPushButton(self.centralwidget)
        self.pushButton_22.setObjectName(u"pushButton_22")
        self.pushButton_22.setGeometry(QRect(1020, 650, 125, 70))
        self.pushButton_22.setFont(font2)
        self.pushButton_22.setStyleSheet(u"background-color: WHITE;\n"
"color: black;\n"
"\n"
"border: 2px solid #d0767f; \n"
"border-radius: 30px; \n"
"padding: 5px;")
        self.pushButton_23 = QPushButton(self.centralwidget)
        self.pushButton_23.setObjectName(u"pushButton_23")
        self.pushButton_23.setGeometry(QRect(709, 730, 125, 70))
        self.pushButton_23.setFont(font2)
        self.pushButton_23.setStyleSheet(u"background-color: WHITE;\n"
"color: black;\n"
"\n"
"border: 2px solid #d0767f; \n"
"border-radius: 30px; \n"
"padding: 5px;")
        self.pushButton_24 = QPushButton(self.centralwidget)
        self.pushButton_24.setObjectName(u"pushButton_24")
        self.pushButton_24.setGeometry(QRect(240, 730, 125, 70))
        self.pushButton_24.setFont(font2)
        self.pushButton_24.setStyleSheet(u"background-color: WHITE;\n"
"color: black;\n"
"\n"
"border: 2px solid #d0767f; \n"
"border-radius: 30px; \n"
"padding: 5px;")
        self.pushButton_25 = QPushButton(self.centralwidget)
        self.pushButton_25.setObjectName(u"pushButton_25")
        self.pushButton_25.setGeometry(QRect(240, 650, 125, 70))
        self.pushButton_25.setFont(font2)
        self.pushButton_25.setStyleSheet(u"background-color: WHITE;\n"
"color: black;\n"
"\n"
"border: 2px solid #d0767f; \n"
"border-radius: 30px; \n"
"padding: 5px;")
        self.pushButton_26 = QPushButton(self.centralwidget)
        self.pushButton_26.setObjectName(u"pushButton_26")
        self.pushButton_26.setGeometry(QRect(1020, 730, 125, 70))
        self.pushButton_26.setFont(font2)
        self.pushButton_26.setStyleSheet(u"background-color: WHITE;\n"
"color: black;\n"
"\n"
"border: 2px solid #d0767f; \n"
"border-radius: 30px; \n"
"padding: 5px;")
        self.pushButton_27 = QPushButton(self.centralwidget)
        self.pushButton_27.setObjectName(u"pushButton_27")
        self.pushButton_27.setGeometry(QRect(860, 730, 125, 70))
        self.pushButton_27.setFont(font2)
        self.pushButton_27.setStyleSheet(u"background-color: WHITE;\n"
"color: black;\n"
"\n"
"border: 2px solid #d0767f; \n"
"border-radius: 30px; \n"
"padding: 5px;")
        self.pushButton_28 = QPushButton(self.centralwidget)
        self.pushButton_28.setObjectName(u"pushButton_28")
        self.pushButton_28.setGeometry(QRect(710, 650, 125, 70))
        self.pushButton_28.setFont(font2)
        self.pushButton_28.setStyleSheet(u"background-color: WHITE;\n"
"color: black;\n"
"\n"
"border: 2px solid #d0767f; \n"
"border-radius: 30px; \n"
"padding: 5px;")
        self.pushButton_31 = QPushButton(self.centralwidget)
        self.pushButton_31.setObjectName(u"pushButton_31")
        self.pushButton_31.setGeometry(QRect(315, 241, 125, 70))
        self.pushButton_31.setFont(font2)
        self.pushButton_31.setStyleSheet(u"background-color: #F2E8DB;\n"
"\n"
"border: 2px solid #F2E8DB; \n"
"border-radius: 30px; \n"
"padding: 5px;")
        icon = QIcon()
        icon.addFile(u"../arrow_back.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_31.setIcon(icon)
        self.pushButton_32 = QPushButton(self.centralwidget)
        self.pushButton_32.setObjectName(u"pushButton_32")
        self.pushButton_32.setGeometry(QRect(1594, 241, 125, 70))
        self.pushButton_32.setFont(font2)
        self.pushButton_32.setStyleSheet(u"background-color: #F2E8DB;\n"
"\n"
"border: 2px solid #F2E8DB; \n"
"border-radius: 30px; \n"
"padding: 5px;")
        icon1 = QIcon()
        icon1.addFile(u"../arrow_forward.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_32.setIcon(icon1)
        self.label_13 = QLabel(self.centralwidget)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(85, 253, 44, 44))
        self.label_13.setFont(font)
        self.label_13.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_13.setStyleSheet(u"color:black;")
        self.label_13.setPixmap(QPixmap(u"../calendar.png"))
        self.label_13.setScaledContents(True)
        self.label_13.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_14 = QLabel(self.centralwidget)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(130, 260, 181, 44))
        self.label_14.setFont(font)
        self.label_14.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_14.setStyleSheet(u"color:black;")
        self.label_14.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_15 = QLabel(self.centralwidget)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(0, 1024, 1920, 56))
        self.label_15.setFont(font)
        self.label_15.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_15.setStyleSheet(u"background-color:black;")
        self.label_15.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.pushButton_29 = QPushButton(self.centralwidget)
        self.pushButton_29.setObjectName(u"pushButton_29")
        self.pushButton_29.setGeometry(QRect(860, 810, 125, 70))
        self.pushButton_29.setFont(font2)
        self.pushButton_29.setStyleSheet(u"background-color: WHITE;\n"
"color: black;\n"
"\n"
"border: 2px solid #d0767f; \n"
"border-radius: 30px; \n"
"padding: 5px;")
        self.pushButton_30 = QPushButton(self.centralwidget)
        self.pushButton_30.setObjectName(u"pushButton_30")
        self.pushButton_30.setGeometry(QRect(240, 810, 125, 70))
        self.pushButton_30.setFont(font2)
        self.pushButton_30.setStyleSheet(u"background-color: WHITE;\n"
"color: black;\n"
"\n"
"border: 2px solid #d0767f; \n"
"border-radius: 30px; \n"
"padding: 5px;")
        self.pushButton_33 = QPushButton(self.centralwidget)
        self.pushButton_33.setObjectName(u"pushButton_33")
        self.pushButton_33.setGeometry(QRect(390, 810, 125, 70))
        self.pushButton_33.setFont(font2)
        self.pushButton_33.setStyleSheet(u"background-color: WHITE;\n"
"color: black;\n"
"\n"
"border: 2px solid #d0767f; \n"
"border-radius: 30px; \n"
"padding: 5px;")
        self.pushButton_34 = QPushButton(self.centralwidget)
        self.pushButton_34.setObjectName(u"pushButton_34")
        self.pushButton_34.setGeometry(QRect(1020, 810, 125, 70))
        self.pushButton_34.setFont(font2)
        self.pushButton_34.setStyleSheet(u"background-color: WHITE;\n"
"color: black;\n"
"\n"
"border: 2px solid #d0767f; \n"
"border-radius: 30px; \n"
"padding: 5px;")
        self.pushButton_35 = QPushButton(self.centralwidget)
        self.pushButton_35.setObjectName(u"pushButton_35")
        self.pushButton_35.setGeometry(QRect(553, 810, 125, 70))
        self.pushButton_35.setFont(font2)
        self.pushButton_35.setStyleSheet(u"background-color: WHITE;\n"
"color: black;\n"
"\n"
"border: 2px solid #d0767f; \n"
"border-radius: 30px; \n"
"padding: 5px;")
        self.pushButton_36 = QPushButton(self.centralwidget)
        self.pushButton_36.setObjectName(u"pushButton_36")
        self.pushButton_36.setGeometry(QRect(80, 810, 125, 70))
        self.pushButton_36.setFont(font2)
        self.pushButton_36.setStyleSheet(u"background-color: WHITE;\n"
"color: black;\n"
"\n"
"border: 2px solid #d0767f; \n"
"border-radius: 30px; \n"
"padding: 5px;")
        self.pushButton_37 = QPushButton(self.centralwidget)
        self.pushButton_37.setObjectName(u"pushButton_37")
        self.pushButton_37.setGeometry(QRect(709, 810, 125, 70))
        self.pushButton_37.setFont(font2)
        self.pushButton_37.setStyleSheet(u"background-color: WHITE;\n"
"color: black;\n"
"\n"
"border: 2px solid #d0767f; \n"
"border-radius: 30px; \n"
"padding: 5px;")
        self.pushButton_38 = QPushButton(self.centralwidget)
        self.pushButton_38.setObjectName(u"pushButton_38")
        self.pushButton_38.setGeometry(QRect(709, 890, 125, 70))
        self.pushButton_38.setFont(font2)
        self.pushButton_38.setStyleSheet(u"background-color: WHITE;\n"
"color: black;\n"
"\n"
"border: 2px solid #d0767f; \n"
"border-radius: 30px; \n"
"padding: 5px;")
        self.pushButton_39 = QPushButton(self.centralwidget)
        self.pushButton_39.setObjectName(u"pushButton_39")
        self.pushButton_39.setGeometry(QRect(860, 890, 125, 70))
        self.pushButton_39.setFont(font2)
        self.pushButton_39.setStyleSheet(u"background-color: WHITE;\n"
"color: black;\n"
"\n"
"border: 2px solid #d0767f; \n"
"border-radius: 30px; \n"
"padding: 5px;")
        self.pushButton_40 = QPushButton(self.centralwidget)
        self.pushButton_40.setObjectName(u"pushButton_40")
        self.pushButton_40.setGeometry(QRect(553, 890, 125, 70))
        self.pushButton_40.setFont(font2)
        self.pushButton_40.setStyleSheet(u"background-color: WHITE;\n"
"color: black;\n"
"\n"
"border: 2px solid #d0767f; \n"
"border-radius: 30px; \n"
"padding: 5px;")
        self.pushButton_41 = QPushButton(self.centralwidget)
        self.pushButton_41.setObjectName(u"pushButton_41")
        self.pushButton_41.setGeometry(QRect(1020, 890, 125, 70))
        self.pushButton_41.setFont(font2)
        self.pushButton_41.setStyleSheet(u"background-color: WHITE;\n"
"color: black;\n"
"\n"
"border: 2px solid #d0767f; \n"
"border-radius: 30px; \n"
"padding: 5px;")
        self.pushButton_42 = QPushButton(self.centralwidget)
        self.pushButton_42.setObjectName(u"pushButton_42")
        self.pushButton_42.setGeometry(QRect(390, 890, 125, 70))
        self.pushButton_42.setFont(font2)
        self.pushButton_42.setStyleSheet(u"background-color: WHITE;\n"
"color: black;\n"
"\n"
"border: 2px solid #d0767f; \n"
"border-radius: 30px; \n"
"padding: 5px;")
        self.pushButton_43 = QPushButton(self.centralwidget)
        self.pushButton_43.setObjectName(u"pushButton_43")
        self.pushButton_43.setGeometry(QRect(240, 890, 125, 70))
        self.pushButton_43.setFont(font2)
        self.pushButton_43.setStyleSheet(u"background-color: WHITE;\n"
"color: black;\n"
"\n"
"border: 2px solid #d0767f; \n"
"border-radius: 30px; \n"
"padding: 5px;")
        self.pushButton_44 = QPushButton(self.centralwidget)
        self.pushButton_44.setObjectName(u"pushButton_44")
        self.pushButton_44.setGeometry(QRect(80, 890, 125, 70))
        self.pushButton_44.setFont(font2)
        self.pushButton_44.setStyleSheet(u"background-color: WHITE;\n"
"color: black;\n"
"\n"
"border: 2px solid #d0767f; \n"
"border-radius: 30px; \n"
"padding: 5px;")
        MainWindow.setCentralWidget(self.centralwidget)
        self.label.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.line.raise_()
        self.line_2.raise_()
        self.label_6.raise_()
        self.label_7.raise_()
        self.label_8.raise_()
        self.label_9.raise_()
        self.label_10.raise_()
        self.label_11.raise_()
        self.label_12.raise_()
        self.line_3.raise_()
        self.pushButton_1.raise_()
        self.pushButton_2.raise_()
        self.pushButton_3.raise_()
        self.pushButton_4.raise_()
        self.pushButton_5.raise_()
        self.pushButton_6.raise_()
        self.pushButton_7.raise_()
        self.pushButton_8.raise_()
        self.pushButton_9.raise_()
        self.pushButton_10.raise_()
        self.pushButton_11.raise_()
        self.pushButton_12.raise_()
        self.pushButton_13.raise_()
        self.pushButton_14.raise_()
        self.pushButton_15.raise_()
        self.pushButton_16.raise_()
        self.pushButton_17.raise_()
        self.pushButton_18.raise_()
        self.pushButton_19.raise_()
        self.pushButton_20.raise_()
        self.pushButton_21.raise_()
        self.pushButton_22.raise_()
        self.pushButton_23.raise_()
        self.pushButton_24.raise_()
        self.pushButton_25.raise_()
        self.pushButton_26.raise_()
        self.pushButton_27.raise_()
        self.pushButton_28.raise_()
        self.pushButton_31.raise_()
        self.pushButton_32.raise_()
        self.label_13.raise_()
        self.label_14.raise_()
        self.label_15.raise_()
        self.pushButton_29.raise_()
        self.pushButton_30.raise_()
        self.pushButton_33.raise_()
        self.pushButton_34.raise_()
        self.pushButton_35.raise_()
        self.pushButton_36.raise_()
        self.pushButton_37.raise_()
        self.pushButton_38.raise_()
        self.pushButton_39.raise_()
        self.pushButton_40.raise_()
        self.pushButton_41.raise_()
        self.pushButton_42.raise_()
        self.pushButton_43.raise_()
        self.pushButton_44.raise_()

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText("")
        self.label_5.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Fecha: 12/09/2025", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Septiembre", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"L", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"M", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"J", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"V", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"D", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"S", None))
        self.pushButton_1.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"13", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"11", None))
        self.pushButton_11.setText(QCoreApplication.translate("MainWindow", u"10", None))
        self.pushButton_12.setText(QCoreApplication.translate("MainWindow", u"14", None))
        self.pushButton_13.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.pushButton_14.setText(QCoreApplication.translate("MainWindow", u"12", None))
        self.pushButton_15.setText(QCoreApplication.translate("MainWindow", u"20", None))
        self.pushButton_16.setText(QCoreApplication.translate("MainWindow", u"22", None))
        self.pushButton_17.setText(QCoreApplication.translate("MainWindow", u"24", None))
        self.pushButton_18.setText(QCoreApplication.translate("MainWindow", u"25", None))
        self.pushButton_19.setText(QCoreApplication.translate("MainWindow", u"15", None))
        self.pushButton_20.setText(QCoreApplication.translate("MainWindow", u"18", None))
        self.pushButton_21.setText(QCoreApplication.translate("MainWindow", u"17", None))
        self.pushButton_22.setText(QCoreApplication.translate("MainWindow", u"21", None))
        self.pushButton_23.setText(QCoreApplication.translate("MainWindow", u"26", None))
        self.pushButton_24.setText(QCoreApplication.translate("MainWindow", u"23", None))
        self.pushButton_25.setText(QCoreApplication.translate("MainWindow", u"16", None))
        self.pushButton_26.setText(QCoreApplication.translate("MainWindow", u"28", None))
        self.pushButton_27.setText(QCoreApplication.translate("MainWindow", u"27", None))
        self.pushButton_28.setText(QCoreApplication.translate("MainWindow", u"19", None))
        self.pushButton_31.setText("")
        self.pushButton_32.setText("")
        self.label_13.setText("")
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Calendario", None))
        self.label_15.setText("")
        self.pushButton_29.setText(QCoreApplication.translate("MainWindow", u"x", None))
        self.pushButton_30.setText(QCoreApplication.translate("MainWindow", u"30", None))
        self.pushButton_33.setText(QCoreApplication.translate("MainWindow", u"31", None))
        self.pushButton_34.setText(QCoreApplication.translate("MainWindow", u"x", None))
        self.pushButton_35.setText(QCoreApplication.translate("MainWindow", u"x", None))
        self.pushButton_36.setText(QCoreApplication.translate("MainWindow", u"29", None))
        self.pushButton_37.setText(QCoreApplication.translate("MainWindow", u"x", None))
        self.pushButton_38.setText(QCoreApplication.translate("MainWindow", u"x", None))
        self.pushButton_39.setText(QCoreApplication.translate("MainWindow", u"x", None))
        self.pushButton_40.setText(QCoreApplication.translate("MainWindow", u"x", None))
        self.pushButton_41.setText(QCoreApplication.translate("MainWindow", u"x", None))
        self.pushButton_42.setText(QCoreApplication.translate("MainWindow", u"x", None))
        self.pushButton_43.setText(QCoreApplication.translate("MainWindow", u"x", None))
        self.pushButton_44.setText(QCoreApplication.translate("MainWindow", u"x", None))
    # retranslateUi

