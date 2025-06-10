# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'item.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGraphicsView, QHBoxLayout,
    QLabel, QProgressBar, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(240, 505)
        self.widgetItem = QWidget(Form)
        self.widgetItem.setObjectName(u"widgetItem")
        self.widgetItem.setGeometry(QRect(0, 0, 231, 501))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widgetItem.sizePolicy().hasHeightForWidth())
        self.widgetItem.setSizePolicy(sizePolicy)
        self.widgetItem.setMinimumSize(QSize(0, 451))
        self.widgetItem.setBaseSize(QSize(0, 455))
        self.widgetItem.setStyleSheet(u"background: white;\n"
"border: 2 solid #A5D6A7;\n"
"border-radius: 6px;")
        self.frameItem = QFrame(self.widgetItem)
        self.frameItem.setObjectName(u"frameItem")
        self.frameItem.setGeometry(QRect(10, 10, 211, 481))
        self.frameItem.setStyleSheet(u"border: none;\n"
"")
        self.verticalLayout_2 = QVBoxLayout(self.frameItem)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.viewItem = QGraphicsView(self.frameItem)
        self.viewItem.setObjectName(u"viewItem")
        self.viewItem.setMinimumSize(QSize(170, 170))
        self.viewItem.setStyleSheet(u"border-radius: 6px;\n"
"border: 2 solid rgb(255, 170, 127);\n"
"")

        self.verticalLayout_2.addWidget(self.viewItem)

        self.labelNameItem = QLabel(self.frameItem)
        self.labelNameItem.setObjectName(u"labelNameItem")
        self.labelNameItem.setStyleSheet(u"color: rgb(125, 92, 73);\n"
"font-size: 16px;\n"
"font-weight: bold;\n"
"border: none;\n"
"\n"
"")

        self.verticalLayout_2.addWidget(self.labelNameItem)

        self.labelSortItem = QLabel(self.frameItem)
        self.labelSortItem.setObjectName(u"labelSortItem")
        self.labelSortItem.setStyleSheet(u"color: rgb(125, 92, 73);\n"
"font-size: 14px;\n"
"border: none;\n"
"")

        self.verticalLayout_2.addWidget(self.labelSortItem)

        self.labelSortItem_2 = QLabel(self.frameItem)
        self.labelSortItem_2.setObjectName(u"labelSortItem_2")
        self.labelSortItem_2.setStyleSheet(u"color: rgb(170, 170, 127);\n"
"font-size: 12px;\n"
"border: none;\n"
"font-weight: bold;")

        self.verticalLayout_2.addWidget(self.labelSortItem_2)

        self.frameWateringItem = QFrame(self.frameItem)
        self.frameWateringItem.setObjectName(u"frameWateringItem")
        self.frameWateringItem.setBaseSize(QSize(0, 0))
        self.horizontalLayout = QHBoxLayout(self.frameWateringItem)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lastWateringItem = QLabel(self.frameWateringItem)
        self.lastWateringItem.setObjectName(u"lastWateringItem")
        self.lastWateringItem.setStyleSheet(u"color: rgb(170, 170, 127);\n"
"font-size: 12px;\n"
"border: none;\n"
"")

        self.horizontalLayout.addWidget(self.lastWateringItem)

        self.label_5 = QLabel(self.frameWateringItem)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"color: rgb(170, 170, 127);\n"
"font-size: 12px;\n"
"border: none;\n"
"")

        self.horizontalLayout.addWidget(self.label_5)

        self.nextWateringItem = QLabel(self.frameWateringItem)
        self.nextWateringItem.setObjectName(u"nextWateringItem")
        self.nextWateringItem.setStyleSheet(u"color: rgb(170, 170, 127);\n"
"font-size: 12px;\n"
"border: none;\n"
"")

        self.horizontalLayout.addWidget(self.nextWateringItem)


        self.verticalLayout_2.addWidget(self.frameWateringItem)

        self.progressWateringItem = QProgressBar(self.frameItem)
        self.progressWateringItem.setObjectName(u"progressWateringItem")
        self.progressWateringItem.setStyleSheet(u"color: white;")
        self.progressWateringItem.setValue(24)

        self.verticalLayout_2.addWidget(self.progressWateringItem)

        self.labelSortItem_3 = QLabel(self.frameItem)
        self.labelSortItem_3.setObjectName(u"labelSortItem_3")
        self.labelSortItem_3.setStyleSheet(u"color: rgb(170, 170, 127);\n"
"font-size: 12px;\n"
"border: none;\n"
"font-weight: bold;")

        self.verticalLayout_2.addWidget(self.labelSortItem_3)

        self.frameFerilizerItem = QFrame(self.frameItem)
        self.frameFerilizerItem.setObjectName(u"frameFerilizerItem")
        self.horizontalLayout_2 = QHBoxLayout(self.frameFerilizerItem)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.lastFeritilizerItem = QLabel(self.frameFerilizerItem)
        self.lastFeritilizerItem.setObjectName(u"lastFeritilizerItem")
        self.lastFeritilizerItem.setStyleSheet(u"color: rgb(170, 170, 127);\n"
"font-size: 12px;\n"
"border: none;\n"
"")

        self.horizontalLayout_2.addWidget(self.lastFeritilizerItem)

        self.label_7 = QLabel(self.frameFerilizerItem)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setStyleSheet(u"color: rgb(170, 170, 127);\n"
"font-size: 12px;\n"
"border: none;\n"
"")

        self.horizontalLayout_2.addWidget(self.label_7)

        self.nextFeritilizerItem = QLabel(self.frameFerilizerItem)
        self.nextFeritilizerItem.setObjectName(u"nextFeritilizerItem")
        self.nextFeritilizerItem.setStyleSheet(u"color: rgb(170, 170, 127);\n"
"font-size: 12px;\n"
"border: none;\n"
"")

        self.horizontalLayout_2.addWidget(self.nextFeritilizerItem)


        self.verticalLayout_2.addWidget(self.frameFerilizerItem)

        self.progressFeritilizerItem = QProgressBar(self.frameItem)
        self.progressFeritilizerItem.setObjectName(u"progressFeritilizerItem")
        self.progressFeritilizerItem.setStyleSheet(u"color: white;\n"
"")
        self.progressFeritilizerItem.setValue(24)

        self.verticalLayout_2.addWidget(self.progressFeritilizerItem)

        self.btnMoreItem = QPushButton(self.frameItem)
        self.btnMoreItem.setObjectName(u"btnMoreItem")
        self.btnMoreItem.setStyleSheet(u"background-color: rgb(255, 170, 127);\n"
"color: rgb(255, 255, 255);\n"
"border: none;\n"
" border-radius: 10px;\n"
" padding: 10px 20px;\n"
"font-size: 16px;\n"
"font-weight: bold;")

        self.verticalLayout_2.addWidget(self.btnMoreItem)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.labelNameItem.setText(QCoreApplication.translate("Form", u"Name", None))
        self.labelSortItem.setText(QCoreApplication.translate("Form", u"Sort", None))
        self.labelSortItem_2.setText(QCoreApplication.translate("Form", u"Watering", None))
        self.lastWateringItem.setText(QCoreApplication.translate("Form", u"lastWatering", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"-", None))
        self.nextWateringItem.setText(QCoreApplication.translate("Form", u"nextWatering", None))
        self.labelSortItem_3.setText(QCoreApplication.translate("Form", u"Feritilizer", None))
        self.lastFeritilizerItem.setText(QCoreApplication.translate("Form", u"lastFeritilizer", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"-", None))
        self.nextFeritilizerItem.setText(QCoreApplication.translate("Form", u"nextFeritilizer", None))
        self.btnMoreItem.setText(QCoreApplication.translate("Form", u"More", None))
    # retranslateUi

