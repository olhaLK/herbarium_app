# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_plant.ui'
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
from PySide6.QtWidgets import (QApplication, QDateEdit, QDialog, QFrame,
    QGraphicsView, QGroupBox, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QSpinBox, QTextEdit,
    QWidget)

class Ui_addPlant(object):
    def setupUi(self, addPlant):
        if not addPlant.objectName():
            addPlant.setObjectName(u"addPlant")
        addPlant.resize(278, 554)
        addPlant.setStyleSheet(u"background: rgb(251, 255, 237);")
        self.frameAddPlant = QFrame(addPlant)
        self.frameAddPlant.setObjectName(u"frameAddPlant")
        self.frameAddPlant.setGeometry(QRect(0, 0, 271, 481))
        self.frameAddPlant.setFrameShape(QFrame.Shape.StyledPanel)
        self.frameAddPlant.setFrameShadow(QFrame.Shadow.Raised)
        self.addPlantImage = QGraphicsView(self.frameAddPlant)
        self.addPlantImage.setObjectName(u"addPlantImage")
        self.addPlantImage.setGeometry(QRect(30, 20, 211, 171))
        self.addPlantImage.setStyleSheet(u"border-radius: 6px;\n"
"border: 2 solid rgb(255, 170, 127);\n"
"background: white;")
        self.labelNameAddPlant = QLabel(self.frameAddPlant)
        self.labelNameAddPlant.setObjectName(u"labelNameAddPlant")
        self.labelNameAddPlant.setGeometry(QRect(30, 200, 49, 16))
        self.labelNameAddPlant.setStyleSheet(u"color: rgb(125, 92, 73);\n"
"font-size: 16px;\n"
"font-weight: bold;\n"
"border: none;\n"
"")
        self.textEditNameAddPlant = QTextEdit(self.frameAddPlant)
        self.textEditNameAddPlant.setObjectName(u"textEditNameAddPlant")
        self.textEditNameAddPlant.setGeometry(QRect(30, 220, 161, 31))
        self.textEditNameAddPlant.setStyleSheet(u"background: white;\n"
"border: 2 solid #A5D6A7 ;\n"
"border-radius: 6px;\n"
"color: rgb(170, 170, 127);\n"
"font-size: 14px;\n"
"font: 9pt \"Century Gothic\";\n"
"")
        self.labelSortAddPlant = QLabel(self.frameAddPlant)
        self.labelSortAddPlant.setObjectName(u"labelSortAddPlant")
        self.labelSortAddPlant.setGeometry(QRect(30, 260, 49, 16))
        self.labelSortAddPlant.setStyleSheet(u"color: rgb(125, 92, 73);\n"
"font-size: 16px;\n"
"font-weight: bold;\n"
"border: none;\n"
"")
        self.textEditSortAddPlant = QTextEdit(self.frameAddPlant)
        self.textEditSortAddPlant.setObjectName(u"textEditSortAddPlant")
        self.textEditSortAddPlant.setGeometry(QRect(30, 280, 161, 31))
        self.textEditSortAddPlant.setStyleSheet(u"background: white;\n"
"border: 2 solid #A5D6A7 ;\n"
"border-radius: 6px;\n"
"color: rgb(170, 170, 127);\n"
"font-size: 14px;\n"
"font: 9pt \"Century Gothic\";\n"
"")
        self.spinWateringAddPlant = QSpinBox(self.frameAddPlant)
        self.spinWateringAddPlant.setObjectName(u"spinWateringAddPlant")
        self.spinWateringAddPlant.setGeometry(QRect(30, 340, 81, 21))
        self.spinWateringAddPlant.setStyleSheet(u"background: white;\n"
"border: 2 solid #A5D6A7 ;\n"
"border-radius: 6px;\n"
"color: rgb(170, 170, 127);\n"
"font-size: 14px;\n"
"font: 9pt \"Century Gothic\";\n"
"")
        self.labelWateringAddPlant = QLabel(self.frameAddPlant)
        self.labelWateringAddPlant.setObjectName(u"labelWateringAddPlant")
        self.labelWateringAddPlant.setGeometry(QRect(30, 310, 161, 31))
        self.labelWateringAddPlant.setStyleSheet(u"color: rgb(125, 92, 73);\n"
"font-size: 16px;\n"
"font-weight: bold;\n"
"border: none;\n"
"")
        self.labelFertilizerAddPlant = QLabel(self.frameAddPlant)
        self.labelFertilizerAddPlant.setObjectName(u"labelFertilizerAddPlant")
        self.labelFertilizerAddPlant.setGeometry(QRect(30, 370, 161, 16))
        self.labelFertilizerAddPlant.setStyleSheet(u"color: rgb(125, 92, 73);\n"
"font-size: 16px;\n"
"font-weight: bold;\n"
"border: none;\n"
"")
        self.spinFertilizerAddPlant = QSpinBox(self.frameAddPlant)
        self.spinFertilizerAddPlant.setObjectName(u"spinFertilizerAddPlant")
        self.spinFertilizerAddPlant.setGeometry(QRect(30, 390, 81, 22))
        self.spinFertilizerAddPlant.setStyleSheet(u"background: white;\n"
"border: 2 solid #A5D6A7 ;\n"
"border-radius: 6px;\n"
"color: rgb(170, 170, 127);\n"
"font-size: 14px;\n"
"font: 9pt \"Century Gothic\";\n"
"")
        self.dateAddPlant = QDateEdit(self.frameAddPlant)
        self.dateAddPlant.setObjectName(u"dateAddPlant")
        self.dateAddPlant.setGeometry(QRect(30, 440, 110, 22))
        self.dateAddPlant.setStyleSheet(u"background: white;\n"
"border: 2 solid #A5D6A7 ;\n"
"border-radius: 6px;\n"
"color: rgb(170, 170, 127);\n"
"font-size: 14px;\n"
"font: 9pt \"Century Gothic\";\n"
"\n"
"")
        self.labelTransplantAddPlant = QLabel(self.frameAddPlant)
        self.labelTransplantAddPlant.setObjectName(u"labelTransplantAddPlant")
        self.labelTransplantAddPlant.setGeometry(QRect(30, 420, 121, 16))
        self.labelTransplantAddPlant.setStyleSheet(u"color: rgb(125, 92, 73);\n"
"font-size: 16px;\n"
"font-weight: bold;\n"
"border: none;\n"
"")
        self.btnAddPlantImage = QPushButton(self.frameAddPlant)
        self.btnAddPlantImage.setObjectName(u"btnAddPlantImage")
        self.btnAddPlantImage.setGeometry(QRect(190, 150, 31, 31))
        self.btnAddPlantImage.setStyleSheet(u"background-color: rgb(255, 194, 217);\n"
"border-radius: 10px;\n"
"color: white;\n"
"")
        self.horizontalGroupBox = QGroupBox(addPlant)
        self.horizontalGroupBox.setObjectName(u"horizontalGroupBox")
        self.horizontalGroupBox.setGeometry(QRect(20, 490, 241, 61))
        self.horizontalGroupBox.setStyleSheet(u"border: none;")
        self.horizontalLayout = QHBoxLayout(self.horizontalGroupBox)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btnBackDelete = QPushButton(self.horizontalGroupBox)
        self.btnBackDelete.setObjectName(u"btnBackDelete")
        self.btnBackDelete.setStyleSheet(u"background-color: #A5D6A7;\n"
"color: #2E7D32;\n"
"border: none;\n"
"border-radius: 6px;\n"
"padding: 10px 20px;\n"
"font-size: 16px;\n"
"font-weight: bold;\n"
"")

        self.horizontalLayout.addWidget(self.btnBackDelete)

        self.btnYesDelete = QPushButton(self.horizontalGroupBox)
        self.btnYesDelete.setObjectName(u"btnYesDelete")
        self.btnYesDelete.setStyleSheet(u"background-color: rgb(255, 88, 91);\n"
"color: white;\n"
"border: none;\n"
"border-radius: 6px;\n"
"padding: 10px 20px;\n"
"font-size: 16px;\n"
"font-weight: bold;\n"
"")

        self.horizontalLayout.addWidget(self.btnYesDelete)


        self.retranslateUi(addPlant)

        QMetaObject.connectSlotsByName(addPlant)
    # setupUi

    def retranslateUi(self, addPlant):
        addPlant.setWindowTitle(QCoreApplication.translate("addPlant", u"Dialog", None))
        self.labelNameAddPlant.setText(QCoreApplication.translate("addPlant", u"Name", None))
        self.labelSortAddPlant.setText(QCoreApplication.translate("addPlant", u"Sort", None))
        self.labelWateringAddPlant.setText(QCoreApplication.translate("addPlant", u"Watering once/day", None))
        self.labelFertilizerAddPlant.setText(QCoreApplication.translate("addPlant", u"Fertilizer once/week", None))
        self.labelTransplantAddPlant.setText(QCoreApplication.translate("addPlant", u"Last transplant", None))
        self.btnAddPlantImage.setText("")
        self.btnBackDelete.setText(QCoreApplication.translate("addPlant", u"Save", None))
        self.btnYesDelete.setText(QCoreApplication.translate("addPlant", u"Cancel", None))
    # retranslateUi

