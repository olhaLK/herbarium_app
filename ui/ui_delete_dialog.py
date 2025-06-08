# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'delete_dialog.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QGroupBox, QHBoxLayout,
    QLabel, QPushButton, QSizePolicy, QWidget)

class Ui_deleteDialog(object):
    def setupUi(self, deleteDialog):
        if not deleteDialog.objectName():
            deleteDialog.setObjectName(u"deleteDialog")
        deleteDialog.resize(407, 300)
        deleteDialog.setStyleSheet(u"background: white;")
        self.horizontalGroupBox = QGroupBox(deleteDialog)
        self.horizontalGroupBox.setObjectName(u"horizontalGroupBox")
        self.horizontalGroupBox.setGeometry(QRect(50, 230, 311, 61))
        self.horizontalGroupBox.setStyleSheet(u"border: none;")
        self.horizontalLayout = QHBoxLayout(self.horizontalGroupBox)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
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

        self.label = QLabel(deleteDialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 60, 371, 51))
        self.label.setStyleSheet(u"color: rgb(125, 92, 73);\n"
"font-size: 18px;\n"
"font-weight: bold;\n"
"border: none;\n"
"")
        self.label_2 = QLabel(deleteDialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(50, 130, 321, 41))
        self.label_2.setStyleSheet(u"color: rgb(136, 1, 3);\n"
"font-size: 16px;\n"
"border: none;\n"
"")

        self.retranslateUi(deleteDialog)

        QMetaObject.connectSlotsByName(deleteDialog)
    # setupUi

    def retranslateUi(self, deleteDialog):
        deleteDialog.setWindowTitle(QCoreApplication.translate("deleteDialog", u"Dialog", None))
        self.btnYesDelete.setText(QCoreApplication.translate("deleteDialog", u"Yes", None))
        self.btnBackDelete.setText(QCoreApplication.translate("deleteDialog", u"Back", None))
        self.label.setText(QCoreApplication.translate("deleteDialog", u"Are you sure you want to delete this plant?", None))
        self.label_2.setText(QCoreApplication.translate("deleteDialog", u"All associated data will be permanently lost", None))
    # retranslateUi

