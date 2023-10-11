# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'cacl.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
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
from PySide6.QtWidgets import (QApplication, QLineEdit, QPushButton, QSizePolicy,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(300, 371)
        self.output = QLineEdit(Form)
        self.output.setObjectName(u"output")
        self.output.setGeometry(QRect(10, 10, 271, 41))
        self.output.setReadOnly(True)
        self.pb9 = QPushButton(Form)
        self.pb9.setObjectName(u"pb9")
        self.pb9.setGeometry(QRect(200, 80, 51, 51))
        self.pb8 = QPushButton(Form)
        self.pb8.setObjectName(u"pb8")
        self.pb8.setGeometry(QRect(120, 80, 51, 51))
        self.pb7 = QPushButton(Form)
        self.pb7.setObjectName(u"pb7")
        self.pb7.setGeometry(QRect(40, 80, 51, 51))
        self.pb5 = QPushButton(Form)
        self.pb5.setObjectName(u"pb5")
        self.pb5.setGeometry(QRect(120, 140, 51, 51))
        self.pb4 = QPushButton(Form)
        self.pb4.setObjectName(u"pb4")
        self.pb4.setGeometry(QRect(40, 140, 51, 51))
        self.pb6 = QPushButton(Form)
        self.pb6.setObjectName(u"pb6")
        self.pb6.setGeometry(QRect(200, 140, 51, 51))
        self.pb2 = QPushButton(Form)
        self.pb2.setObjectName(u"pb2")
        self.pb2.setGeometry(QRect(120, 200, 51, 51))
        self.pb3 = QPushButton(Form)
        self.pb3.setObjectName(u"pb3")
        self.pb3.setGeometry(QRect(200, 200, 51, 51))
        self.pb1 = QPushButton(Form)
        self.pb1.setObjectName(u"pb1")
        self.pb1.setGeometry(QRect(40, 200, 51, 51))
        self.pbminus = QPushButton(Form)
        self.pbminus.setObjectName(u"pbminus")
        self.pbminus.setGeometry(QRect(80, 260, 31, 23))
        self.pbtimes = QPushButton(Form)
        self.pbtimes.setObjectName(u"pbtimes")
        self.pbtimes.setGeometry(QRect(110, 260, 41, 23))
        self.pbdivide = QPushButton(Form)
        self.pbdivide.setObjectName(u"pbdivide")
        self.pbdivide.setGeometry(QRect(150, 260, 51, 23))
        self.pbaplus = QPushButton(Form)
        self.pbaplus.setObjectName(u"pbaplus")
        self.pbaplus.setGeometry(QRect(41, 261, 41, 23))
        self.pbequal = QPushButton(Form)
        self.pbequal.setObjectName(u"pbequal")
        self.pbequal.setGeometry(QRect(120, 290, 75, 23))
        self.pbdot = QPushButton(Form)
        self.pbdot.setObjectName(u"pbdot")
        self.pbdot.setGeometry(QRect(40, 290, 75, 23))
        self.pb0 = QPushButton(Form)
        self.pb0.setObjectName(u"pb0")
        self.pb0.setGeometry(QRect(200, 250, 51, 51))
        self.AC = QPushButton(Form)
        self.AC.setObjectName(u"AC")
        self.AC.setGeometry(QRect(40, 320, 75, 24))
        self.Delete = QPushButton(Form)
        self.Delete.setObjectName(u"Delete")
        self.Delete.setGeometry(QRect(160, 320, 75, 24))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Cacl", None))
        self.pb9.setText(QCoreApplication.translate("Form", u"9", None))
        self.pb8.setText(QCoreApplication.translate("Form", u"8", None))
        self.pb7.setText(QCoreApplication.translate("Form", u"7", None))
        self.pb5.setText(QCoreApplication.translate("Form", u"5", None))
        self.pb4.setText(QCoreApplication.translate("Form", u"4", None))
        self.pb6.setText(QCoreApplication.translate("Form", u"6", None))
        self.pb2.setText(QCoreApplication.translate("Form", u"2", None))
        self.pb3.setText(QCoreApplication.translate("Form", u"3", None))
        self.pb1.setText(QCoreApplication.translate("Form", u"1", None))
        self.pbminus.setText(QCoreApplication.translate("Form", u"-", None))
        self.pbtimes.setText(QCoreApplication.translate("Form", u"*", None))
        self.pbdivide.setText(QCoreApplication.translate("Form", u"/", None))
        self.pbaplus.setText(QCoreApplication.translate("Form", u"+", None))
        self.pbequal.setText(QCoreApplication.translate("Form", u"=", None))
        self.pbdot.setText(QCoreApplication.translate("Form", u".", None))
        self.pb0.setText(QCoreApplication.translate("Form", u"0", None))
        self.AC.setText(QCoreApplication.translate("Form", u"AC", None))
        self.Delete.setText(QCoreApplication.translate("Form", u"Delete", None))
    # retranslateUi

