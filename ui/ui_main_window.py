# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QScrollArea,
    QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(863, 853)
        MainWindow.setMouseTracking(True)
        MainWindow.setStyleSheet(u"background: rgb(251, 255, 237);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QSize(0, 30))
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setMinimumSize(QSize(0, 50))
        self.filterMain = QComboBox(self.widget)
        self.filterMain.setObjectName(u"filterMain")
        self.filterMain.setGeometry(QRect(10, 0, 231, 31))
        self.filterMain.setStyleSheet(u"background: white;\n"
"border: 2 solid #A5D6A7 ;\n"
"border-radius: 6px;\n"
"color: rgb(125, 92, 73);\n"
"font-size: 14px;")
        self.searchMain = QLineEdit(self.widget)
        self.searchMain.setObjectName(u"searchMain")
        self.searchMain.setGeometry(QRect(330, 0, 241, 31))
        self.searchMain.setStyleSheet(u"background-color: #FFFFFF;\n"
"border: 2px solid #A5D6A7;\n"
"padding: 5px;\n"
"border-radius: 6px;\n"
"color: rgb(125, 92, 73);\n"
"font-size: 14px;\n"
"")
        self.btnSearchMain = QPushButton(self.widget)
        self.btnSearchMain.setObjectName(u"btnSearchMain")
        self.btnSearchMain.setGeometry(QRect(570, 0, 41, 31))
        self.btnSearchMain.setStyleSheet(u"border: 2 solid rgb(255, 170, 127);\n"
"background: rgb(255, 170, 127);\n"
"border-radius: 6px;\n"
"color: white;")
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.EditFind))
        self.btnSearchMain.setIcon(icon)
        self.btnAddMain = QPushButton(self.widget)
        self.btnAddMain.setObjectName(u"btnAddMain")
        self.btnAddMain.setGeometry(QRect(680, 0, 101, 31))
        self.btnAddMain.setMouseTracking(False)
        self.btnAddMain.setContextMenuPolicy(Qt.ContextMenuPolicy.ActionsContextMenu)
        self.btnAddMain.setStyleSheet(u"background-color: #A5D6A7;\n"
"color: #2E7D32;\n"
"border: none;\n"
"border-radius: 6px;\n"
"padding: 10px 20px;\n"
"font-size: 16px;\n"
"font: 9pt \"Century Gothic\";\n"
"font-weight: bold;\n"
"\n"
"")
        self.btnAddMain.setLocale(QLocale(QLocale.English, QLocale.Barbados))

        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)

        self.scrollAreaMain = QScrollArea(self.centralwidget)
        self.scrollAreaMain.setObjectName(u"scrollAreaMain")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.scrollAreaMain.sizePolicy().hasHeightForWidth())
        self.scrollAreaMain.setSizePolicy(sizePolicy1)
        self.scrollAreaMain.setMinimumSize(QSize(0, 0))
        self.scrollAreaMain.setStyleSheet(u"border: none;")
        self.scrollAreaMain.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        sizePolicy1.setHeightForWidth(self.scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents.setSizePolicy(sizePolicy1)
        self.scrollAreaWidgetContents.setMinimumSize(QSize(0, 0))
        self.scrollAreaWidgetContents.setMaximumSize(QSize(16777215, 16777215))
        self.scrollAreaWidgetContents.setMouseTracking(True)
        self.scrollAreaWidgetContents.setStyleSheet(u"")
        self.scrollAreaMain.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout.addWidget(self.scrollAreaMain, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.scrollAreaMain.raise_()
        self.widget.raise_()
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 863, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btnSearchMain.setText("")
        self.btnAddMain.setText(QCoreApplication.translate("MainWindow", u"Add", None))
    # retranslateUi

