# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'item_full.ui'
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
from PySide6.QtWidgets import (QApplication, QDateEdit, QFrame, QGraphicsView,
    QGroupBox, QHBoxLayout, QLabel, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QSpinBox,
    QStatusBar, QTextEdit, QWidget)

class Ui_itemFull(object):
    def setupUi(self, itemFull):
        if not itemFull.objectName():
            itemFull.setObjectName(u"itemFull")
        itemFull.resize(782, 571)
        itemFull.setStyleSheet(u"background: rgb(251, 255, 237);")
        self.centralwidget = QWidget(itemFull)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frameItemFull = QFrame(self.centralwidget)
        self.frameItemFull.setObjectName(u"frameItemFull")
        self.frameItemFull.setGeometry(QRect(40, 30, 711, 481))
        self.frameItemFull.setFrameShape(QFrame.Shape.StyledPanel)
        self.frameItemFull.setFrameShadow(QFrame.Shadow.Raised)
        self.viewItemFull = QGraphicsView(self.frameItemFull)
        self.viewItemFull.setObjectName(u"viewItemFull")
        self.viewItemFull.setGeometry(QRect(20, 20, 251, 231))
        self.viewItemFull.setStyleSheet(u"border-radius: 6px;\n"
"border: 2 solid rgb(255, 170, 127);\n"
"background: white;")
        self.changeImageItemFull = QPushButton(self.frameItemFull)
        self.changeImageItemFull.setObjectName(u"changeImageItemFull")
        self.changeImageItemFull.setGeometry(QRect(220, 200, 31, 31))
        self.changeImageItemFull.setStyleSheet(u"background-color: rgb(255, 194, 217);\n"
"border-radius: 10px;\n"
"color: white;\n"
"")
        self.textEditNameItemFull = QTextEdit(self.frameItemFull)
        self.textEditNameItemFull.setObjectName(u"textEditNameItemFull")
        self.textEditNameItemFull.setGeometry(QRect(370, 60, 241, 31))
        self.textEditNameItemFull.setStyleSheet(u"background: white;\n"
"border: 2 solid #A5D6A7 ;\n"
"border-radius: 6px;\n"
"color: rgb(170, 170, 127);\n"
"font-size: 14px;\n"
"font: 9pt \"Century Gothic\";\n"
"")
        self.textEditSortItemFull = QTextEdit(self.frameItemFull)
        self.textEditSortItemFull.setObjectName(u"textEditSortItemFull")
        self.textEditSortItemFull.setGeometry(QRect(370, 120, 241, 31))
        self.textEditSortItemFull.setStyleSheet(u"background: white;\n"
"border: 2 solid #A5D6A7 ;\n"
"border-radius: 6px;\n"
"color: rgb(170, 170, 127);\n"
"font-size: 14px;\n"
"font: 9pt \"Century Gothic\";\n"
"")
        self.spinWateringItemFull = QSpinBox(self.frameItemFull)
        self.spinWateringItemFull.setObjectName(u"spinWateringItemFull")
        self.spinWateringItemFull.setGeometry(QRect(20, 300, 81, 21))
        self.spinWateringItemFull.setStyleSheet(u"background: white;\n"
"border: 2 solid #A5D6A7 ;\n"
"border-radius: 6px;\n"
"color: rgb(170, 170, 127);\n"
"font-size: 14px;\n"
"font: 9pt \"Century Gothic\";\n"
"")
        self.label_3 = QLabel(self.frameItemFull)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 270, 151, 31))
        self.label_3.setStyleSheet(u"color: rgb(125, 92, 73);\n"
"font-size: 16px;\n"
"font-weight: bold;\n"
"border: none;\n"
"")
        self.label_4 = QLabel(self.frameItemFull)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(190, 270, 161, 31))
        self.label_4.setStyleSheet(u"color: rgb(125, 92, 73);\n"
"font-size: 16px;\n"
"font-weight: bold;\n"
"border: none;\n"
"")
        self.spinFeritilizerItem = QSpinBox(self.frameItemFull)
        self.spinFeritilizerItem.setObjectName(u"spinFeritilizerItem")
        self.spinFeritilizerItem.setGeometry(QRect(190, 300, 81, 21))
        self.spinFeritilizerItem.setStyleSheet(u"background: white;\n"
"border: 2 solid #A5D6A7 ;\n"
"border-radius: 6px;\n"
"color: rgb(170, 170, 127);\n"
"font-size: 14px;\n"
"font: 9pt \"Century Gothic\";\n"
"")
        self.labelSortItemFull = QLabel(self.frameItemFull)
        self.labelSortItemFull.setObjectName(u"labelSortItemFull")
        self.labelSortItemFull.setGeometry(QRect(370, 100, 49, 16))
        self.labelSortItemFull.setStyleSheet(u"color: rgb(125, 92, 73);\n"
"font-size: 16px;\n"
"font-weight: bold;\n"
"border: none;\n"
"")
        self.labelNameItemFull = QLabel(self.frameItemFull)
        self.labelNameItemFull.setObjectName(u"labelNameItemFull")
        self.labelNameItemFull.setGeometry(QRect(370, 40, 49, 16))
        self.labelNameItemFull.setStyleSheet(u"color: rgb(125, 92, 73);\n"
"font-size: 16px;\n"
"font-weight: bold;\n"
"border: none;\n"
"")
        self.dateLastWateringItem = QDateEdit(self.frameItemFull)
        self.dateLastWateringItem.setObjectName(u"dateLastWateringItem")
        self.dateLastWateringItem.setGeometry(QRect(20, 360, 110, 22))
        self.dateLastWateringItem.setStyleSheet(u"background: white;\n"
"border: 2 solid #A5D6A7 ;\n"
"border-radius: 6px;\n"
"color: rgb(170, 170, 127);\n"
"font-size: 14px;\n"
"font: 9pt \"Century Gothic\";\n"
"")
        self.label_5 = QLabel(self.frameItemFull)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(20, 330, 131, 31))
        self.label_5.setStyleSheet(u"color: rgb(125, 92, 73);\n"
"font-size: 16px;\n"
"font-weight: bold;\n"
"border: none;\n"
"")
        self.label_6 = QLabel(self.frameItemFull)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(190, 335, 131, 21))
        self.label_6.setStyleSheet(u"color: rgb(125, 92, 73);\n"
"font-size: 16px;\n"
"font-weight: bold;\n"
"border: none;\n"
"")
        self.dateLastFeritilizerItem = QDateEdit(self.frameItemFull)
        self.dateLastFeritilizerItem.setObjectName(u"dateLastFeritilizerItem")
        self.dateLastFeritilizerItem.setGeometry(QRect(190, 360, 110, 22))
        self.dateLastFeritilizerItem.setStyleSheet(u"background: white;\n"
"border: 2 solid #A5D6A7 ;\n"
"border-radius: 6px;\n"
"color: rgb(170, 170, 127);\n"
"font-size: 14px;\n"
"font: 9pt \"Century Gothic\";\n"
"")
        self.textEditDescriptionItemFull = QTextEdit(self.frameItemFull)
        self.textEditDescriptionItemFull.setObjectName(u"textEditDescriptionItemFull")
        self.textEditDescriptionItemFull.setGeometry(QRect(370, 190, 241, 191))
        self.textEditDescriptionItemFull.setStyleSheet(u"background: white;\n"
"border: 2 solid #A5D6A7 ;\n"
"border-radius: 6px;\n"
"color: rgb(170, 170, 127);\n"
"font-size: 14px;\n"
"font: 9pt \"Century Gothic\";\n"
"")
        self.labelDescriptionItemFull = QLabel(self.frameItemFull)
        self.labelDescriptionItemFull.setObjectName(u"labelDescriptionItemFull")
        self.labelDescriptionItemFull.setGeometry(QRect(370, 170, 101, 16))
        self.labelDescriptionItemFull.setStyleSheet(u"color: rgb(125, 92, 73);\n"
"font-size: 16px;\n"
"font-weight: bold;\n"
"border: none;\n"
"")
        self.horizontalGroupBox = QGroupBox(self.frameItemFull)
        self.horizontalGroupBox.setObjectName(u"horizontalGroupBox")
        self.horizontalGroupBox.setGeometry(QRect(230, 410, 271, 71))
        self.horizontalGroupBox.setStyleSheet(u"")
        self.horizontalLayout = QHBoxLayout(self.horizontalGroupBox)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btnSaveItem = QPushButton(self.horizontalGroupBox)
        self.btnSaveItem.setObjectName(u"btnSaveItem")
        self.btnSaveItem.setStyleSheet(u"background-color: #A5D6A7;\n"
"color: #2E7D32;\n"
"border: none;\n"
"border-radius: 6px;\n"
"padding: 10px 20px;\n"
"font-size: 16px;\n"
"font: \"Century Gothic\";\n"
"font-weight: bold;\n"
"")

        self.horizontalLayout.addWidget(self.btnSaveItem)

        self.btnBackItem = QPushButton(self.horizontalGroupBox)
        self.btnBackItem.setObjectName(u"btnBackItem")
        self.btnBackItem.setStyleSheet(u"background-color: #A5D6A7;\n"
"color: #2E7D32;\n"
"border: none;\n"
"border-radius: 6px;\n"
"padding: 10px 20px;\n"
"font-size: 16px;\n"
"font-weight: bold;\n"
"")

        self.horizontalLayout.addWidget(self.btnBackItem)

        self.btnDeleteItem = QPushButton(self.horizontalGroupBox)
        self.btnDeleteItem.setObjectName(u"btnDeleteItem")
        self.btnDeleteItem.setStyleSheet(u"background-color: rgb(255, 88, 91);\n"
"color: white;\n"
"border: none;\n"
"border-radius: 6px;\n"
"padding: 10px 20px;\n"
"font-size: 16px;\n"
"font-weight: bold;\n"
"")

        self.horizontalLayout.addWidget(self.btnDeleteItem)

        self.viewItemFull.raise_()
        self.changeImageItemFull.raise_()
        self.textEditNameItemFull.raise_()
        self.textEditSortItemFull.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.labelSortItemFull.raise_()
        self.labelNameItemFull.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.textEditDescriptionItemFull.raise_()
        self.labelDescriptionItemFull.raise_()
        self.horizontalGroupBox.raise_()
        self.spinWateringItemFull.raise_()
        self.dateLastWateringItem.raise_()
        self.spinFeritilizerItem.raise_()
        self.dateLastFeritilizerItem.raise_()
        itemFull.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(itemFull)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 782, 22))
        itemFull.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(itemFull)
        self.statusbar.setObjectName(u"statusbar")
        itemFull.setStatusBar(self.statusbar)

        self.retranslateUi(itemFull)

        QMetaObject.connectSlotsByName(itemFull)
    # setupUi

    def retranslateUi(self, itemFull):
        itemFull.setWindowTitle(QCoreApplication.translate("itemFull", u"MainWindow", None))
        self.changeImageItemFull.setText("")
        self.label_3.setText(QCoreApplication.translate("itemFull", u"Watering once/day", None))
        self.label_4.setText(QCoreApplication.translate("itemFull", u"Fertilizer once/week", None))
        self.labelSortItemFull.setText(QCoreApplication.translate("itemFull", u"Sort", None))
        self.labelNameItemFull.setText(QCoreApplication.translate("itemFull", u"Name", None))
        self.label_5.setText(QCoreApplication.translate("itemFull", u"Last watering", None))
        self.label_6.setText(QCoreApplication.translate("itemFull", u"Last feritizer", None))
        self.labelDescriptionItemFull.setText(QCoreApplication.translate("itemFull", u"Description", None))
        self.btnSaveItem.setText(QCoreApplication.translate("itemFull", u"Save", None))
        self.btnBackItem.setText(QCoreApplication.translate("itemFull", u"Back", None))
        self.btnDeleteItem.setText(QCoreApplication.translate("itemFull", u"Delete", None))
    # retranslateUi

