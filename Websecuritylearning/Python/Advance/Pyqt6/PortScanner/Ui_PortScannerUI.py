# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PortScannerUI.ui'
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
    QSpacerItem, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(400, 300)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.output = QPlainTextEdit(Form)
        self.output.setObjectName(u"output")
        self.output.setStyleSheet(u"")
        self.output.setTabChangesFocus(False)
        self.output.setReadOnly(True)

        self.gridLayout.addWidget(self.output, 0, 0, 10, 1)

        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(16777215, 13))
        self.label_4.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_4, 0, 6, 1, 1)

        self.label = QLabel(Form)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 1, 1, 1, 1)

        self.sip1 = QLineEdit(Form)
        self.sip1.setObjectName(u"sip1")
        self.sip1.setMaximumSize(QSize(48, 16777215))
        self.sip1.setStyleSheet(u"background-color: rgb(170, 255, 255);")
        self.sip1.setMaxLength(3)
        self.sip1.setFrame(True)
        self.sip1.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.sip1, 1, 2, 1, 1)

        self.sip2 = QLineEdit(Form)
        self.sip2.setObjectName(u"sip2")
        self.sip2.setMaximumSize(QSize(48, 16777215))
        self.sip2.setStyleSheet(u"background-color: rgb(170, 255, 255);")
        self.sip2.setMaxLength(3)
        self.sip2.setFrame(True)
        self.sip2.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.sip2, 1, 3, 1, 1)

        self.sip3 = QLineEdit(Form)
        self.sip3.setObjectName(u"sip3")
        self.sip3.setMaximumSize(QSize(48, 16777215))
        self.sip3.setStyleSheet(u"background-color: rgb(170, 255, 255);")
        self.sip3.setMaxLength(3)
        self.sip3.setFrame(True)
        self.sip3.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.sip3, 1, 4, 1, 1)

        self.label_12 = QLabel(Form)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMaximumSize(QSize(10, 16777215))
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.label_12.setFont(font)

        self.gridLayout.addWidget(self.label_12, 1, 5, 1, 1)

        self.sip4 = QLineEdit(Form)
        self.sip4.setObjectName(u"sip4")
        self.sip4.setStyleSheet(u"background-color: rgb(255, 255, 0);")
        self.sip4.setMaxLength(3)
        self.sip4.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.sip4, 1, 6, 1, 1)

        self.label_5 = QLabel(Form)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(16777215, 15))
        self.label_5.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_5, 2, 6, 1, 1)

        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 3, 1, 1, 1)

        self.dip1 = QLineEdit(Form)
        self.dip1.setObjectName(u"dip1")
        self.dip1.setStyleSheet(u"background-color: rgb(170, 255, 255);")
        self.dip1.setMaxLength(3)
        self.dip1.setAlignment(Qt.AlignCenter)
        self.dip1.setReadOnly(True)

        self.gridLayout.addWidget(self.dip1, 3, 2, 1, 1)

        self.dip2 = QLineEdit(Form)
        self.dip2.setObjectName(u"dip2")
        self.dip2.setStyleSheet(u"background-color: rgb(170, 255, 255);")
        self.dip2.setMaxLength(3)
        self.dip2.setAlignment(Qt.AlignCenter)
        self.dip2.setReadOnly(True)

        self.gridLayout.addWidget(self.dip2, 3, 3, 1, 1)

        self.dip3 = QLineEdit(Form)
        self.dip3.setObjectName(u"dip3")
        self.dip3.setStyleSheet(u"background-color: rgb(170, 255, 255);")
        self.dip3.setMaxLength(3)
        self.dip3.setAlignment(Qt.AlignCenter)
        self.dip3.setReadOnly(True)

        self.gridLayout.addWidget(self.dip3, 3, 4, 1, 1)

        self.label_13 = QLabel(Form)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMaximumSize(QSize(10, 16777215))
        self.label_13.setFont(font)

        self.gridLayout.addWidget(self.label_13, 3, 5, 1, 1)

        self.dip4 = QLineEdit(Form)
        self.dip4.setObjectName(u"dip4")
        self.dip4.setStyleSheet(u"background-color: rgb(255, 255, 0);")
        self.dip4.setMaxLength(3)
        self.dip4.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.dip4, 3, 6, 1, 1)

        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        font1 = QFont()
        font1.setPointSize(9)
        self.label_3.setFont(font1)

        self.gridLayout.addWidget(self.label_3, 4, 1, 1, 1)

        self.label_6 = QLabel(Form)
        self.label_6.setObjectName(u"label_6")
        font2 = QFont()
        font2.setPointSize(8)
        self.label_6.setFont(font2)

        self.gridLayout.addWidget(self.label_6, 4, 6, 1, 1)

        self.label_7 = QLabel(Form)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 5, 1, 1, 1)

        self.sport = QLineEdit(Form)
        self.sport.setObjectName(u"sport")
        self.sport.setStyleSheet(u"background-color: rgb(170, 255, 255);")
        self.sport.setMaxLength(5)

        self.gridLayout.addWidget(self.sport, 5, 2, 1, 1)

        self.label_8 = QLabel(Form)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_8, 5, 3, 1, 1)

        self.eport = QLineEdit(Form)
        self.eport.setObjectName(u"eport")
        self.eport.setStyleSheet(u"background-color: rgb(170, 255, 255);")
        self.eport.setMaxLength(5)

        self.gridLayout.addWidget(self.eport, 5, 4, 1, 1)

        self.label_10 = QLabel(Form)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font2)

        self.gridLayout.addWidget(self.label_10, 5, 6, 1, 1)

        self.label_9 = QLabel(Form)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout.addWidget(self.label_9, 6, 1, 1, 1)

        self.label_11 = QLabel(Form)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout.addWidget(self.label_11, 8, 1, 1, 1)

        self.elapsetime = QLineEdit(Form)
        self.elapsetime.setObjectName(u"elapsetime")
        self.elapsetime.setCursor(QCursor(Qt.ArrowCursor))
        self.elapsetime.setReadOnly(True)

        self.gridLayout.addWidget(self.elapsetime, 8, 2, 1, 3)

        self.verticalSpacer = QSpacerItem(20, 62, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.gridLayout.addItem(self.verticalSpacer, 9, 2, 1, 1)

        self.portlstslct = QComboBox(Form)
        self.portlstslct.setObjectName(u"portlstslct")

        self.gridLayout.addWidget(self.portlstslct, 4, 2, 1, 3)

        self.threadcount = QComboBox(Form)
        self.threadcount.setObjectName(u"threadcount")

        self.gridLayout.addWidget(self.threadcount, 6, 2, 1, 3)

        self.startscan = QPushButton(Form)
        self.startscan.setObjectName(u"startscan")

        self.gridLayout.addWidget(self.startscan, 7, 2, 1, 3)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"PortScanner", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"\u7f51\u6bb5", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u8d77\u59cbIP", None))
        self.sip1.setInputMask("")
        self.sip1.setText("")
        self.sip2.setInputMask("")
        self.sip2.setText("")
        self.sip3.setInputMask("")
        self.sip3.setText("")
        self.label_12.setText(QCoreApplication.translate("Form", u".", None))
        self.sip4.setPlaceholderText(QCoreApplication.translate("Form", u"\u5fc5\u987b", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"\u2193", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u7ec8\u70b9IP(\u53ef\u9009)", None))
        self.label_13.setText(QCoreApplication.translate("Form", u".", None))
#if QT_CONFIG(tooltip)
        self.dip4.setToolTip(QCoreApplication.translate("Form", u"\u53ef\u9009\uff0c\u7a7a\u5219\u53ea\u626b\u63cf\u4e00\u4e2aIP", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.dip4.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.dip4.setPlaceholderText(QCoreApplication.translate("Form", u"\u53ef\u9009", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u5e38\u7528\u7aef\u53e3", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"\u66f4\u5feb\u901f", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"\u7aef\u53e3\u8303\u56f4", None))
        self.sport.setText("")
        self.label_8.setText(QCoreApplication.translate("Form", u"\u2192", None))
        self.eport.setText("")
        self.label_10.setText(QCoreApplication.translate("Form", u"\u8f83\u6162", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"\u7ebf\u7a0b\u6570", None))
        self.label_11.setText(QCoreApplication.translate("Form", u"\u7528\u65f6", None))
        self.startscan.setText(QCoreApplication.translate("Form", u"\u626b\u63cf", None))
    # retranslateUi

