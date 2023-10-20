# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sniffer-233.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QLabel,
    QLineEdit, QPlainTextEdit, QPushButton, QSizePolicy,
    QWidget)
import sniffer_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(419, 731)
        Form.setStyleSheet(u"")
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.startsniff = QPushButton(Form)
        self.startsniff.setObjectName(u"startsniff")
        self.startsniff.setCheckable(True)
        self.startsniff.setChecked(False)

        self.gridLayout.addWidget(self.startsniff, 2, 3, 1, 1)

        self.ptcset = QComboBox(Form)
        self.ptcset.setObjectName(u"ptcset")

        self.gridLayout.addWidget(self.ptcset, 0, 3, 1, 1)

        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        font = QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"color: rgb(255, 0, 0);")

        self.gridLayout.addWidget(self.label_3, 1, 2, 1, 1)

        self.output = QPlainTextEdit(Form)
        self.output.setObjectName(u"output")
        self.output.setStyleSheet(u"background-color: rgb(0, 255, 127);")
        self.output.setReadOnly(True)

        self.gridLayout.addWidget(self.output, 3, 0, 1, 4)

        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setPointSize(12)
        self.label.setFont(font1)
        self.label.setStyleSheet(u"color: rgb(0, 255, 255);")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.srcfil = QLineEdit(Form)
        self.srcfil.setObjectName(u"srcfil")
        self.srcfil.setStyleSheet(u"")
        self.srcfil.setReadOnly(False)

        self.gridLayout.addWidget(self.srcfil, 0, 1, 1, 1)

        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"color: rgb(0, 255, 0);")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.selfip = QLabel(Form)
        self.selfip.setObjectName(u"selfip")
        font2 = QFont()
        font2.setPointSize(13)
        self.selfip.setFont(font2)
        self.selfip.setScaledContents(False)
        self.selfip.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.selfip, 2, 1, 1, 1)

        self.portset = QLineEdit(Form)
        self.portset.setObjectName(u"portset")
        self.portset.setStyleSheet(u"")

        self.gridLayout.addWidget(self.portset, 1, 3, 1, 1)

        self.dstfil = QLineEdit(Form)
        self.dstfil.setObjectName(u"dstfil")
        self.dstfil.setStyleSheet(u"")

        self.gridLayout.addWidget(self.dstfil, 1, 1, 1, 1)

        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)
        self.label_4.setStyleSheet(u"color: rgb(255, 170, 0);")

        self.gridLayout.addWidget(self.label_4, 0, 2, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u6293\u5305", None))
        self.startsniff.setText(QCoreApplication.translate("Form", u"\u6293\u53d6", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u7aef\u53e3", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u6e90", None))
        self.srcfil.setPlaceholderText("")
        self.label_2.setText(QCoreApplication.translate("Form", u"\u76ee\u7684", None))
        self.selfip.setText(QCoreApplication.translate("Form", u"IP", None))
        self.portset.setPlaceholderText("")
        self.dstfil.setPlaceholderText("")
        self.label_4.setText(QCoreApplication.translate("Form", u"\u534f\u8bae", None))
    # retranslateUi

