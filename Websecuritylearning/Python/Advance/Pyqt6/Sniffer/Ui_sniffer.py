# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sniffer.ui'
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

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(368, 299)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(12)
        self.label.setFont(font)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.srcfil = QLineEdit(Form)
        self.srcfil.setObjectName(u"srcfil")
        self.srcfil.setStyleSheet(u"background-color: rgb(170, 255, 255);")
        self.srcfil.setReadOnly(False)

        self.gridLayout.addWidget(self.srcfil, 0, 1, 1, 1)

        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")
        font1 = QFont()
        font1.setPointSize(10)
        self.label_4.setFont(font1)

        self.gridLayout.addWidget(self.label_4, 0, 2, 1, 1)

        self.ptcset = QComboBox(Form)
        self.ptcset.setObjectName(u"ptcset")

        self.gridLayout.addWidget(self.ptcset, 0, 3, 1, 1)

        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font1)

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.desfil = QLineEdit(Form)
        self.desfil.setObjectName(u"desfil")
        self.desfil.setStyleSheet(u"background-color: rgb(170, 255, 255);")

        self.gridLayout.addWidget(self.desfil, 1, 1, 1, 1)

        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)

        self.gridLayout.addWidget(self.label_3, 1, 2, 1, 1)

        self.portset = QLineEdit(Form)
        self.portset.setObjectName(u"portset")
        self.portset.setStyleSheet(u"background-color: rgb(170, 255, 255);")

        self.gridLayout.addWidget(self.portset, 1, 3, 1, 1)

        self.startsniff = QPushButton(Form)
        self.startsniff.setObjectName(u"startsniff")
        self.startsniff.setCheckable(True)
        self.startsniff.setChecked(False)

        self.gridLayout.addWidget(self.startsniff, 2, 3, 1, 1)

        self.output = QPlainTextEdit(Form)
        self.output.setObjectName(u"output")
        self.output.setStyleSheet(u"background-color: rgb(0, 255, 255);\n"
"background-color: rgb(173, 173, 173);")
        self.output.setReadOnly(True)

        self.gridLayout.addWidget(self.output, 3, 0, 1, 4)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"IPSniffer", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u6e90\u5730\u5740", None))
        self.srcfil.setPlaceholderText(QCoreApplication.translate("Form", u"\u7559\u7a7a\u5219\u4e0d\u8fdb\u884c\u7b5b\u9009", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"\u534f\u8bae\u7b5b\u9009", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u76ee\u7684\u5730\u5740", None))
        self.desfil.setPlaceholderText(QCoreApplication.translate("Form", u"\u7559\u7a7a\u5219\u4e0d\u8fdb\u884c\u7b5b\u9009", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u7aef\u53e3\u8bbe\u5b9a", None))
        self.portset.setPlaceholderText(QCoreApplication.translate("Form", u"\u7559\u7a7a\u5219\u968f\u673a\u8bbe\u5b9a", None))
        self.startsniff.setText(QCoreApplication.translate("Form", u"\u6293\u53d6", None))
    # retranslateUi

