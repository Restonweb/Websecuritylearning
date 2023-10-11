"""

THIS IS A SHITTY CODE, NONE FUCTIONAL

"""


from PySide6.QtWidgets import QMainWindow, QApplication, QLineEdit, QWidget
from PySide6.QtCore import Qt
from cacl import Ui_Form
import time

class MyWindow(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.SF = False
        self.RF = False
        self.result = ''
        self.setupUi(self)
        self.bind()

    def bind(self):
        self.pb0.clicked.connect(lambda: self.addnum('0'))
        self.pb1.clicked.connect(lambda: self.addnum('1'))
        self.pb2.clicked.connect(lambda: self.addnum('2'))
        self.pb3.clicked.connect(lambda: self.addnum('3'))
        self.pb4.clicked.connect(lambda: self.addnum('4'))
        self.pb5.clicked.connect(lambda: self.addnum('5'))
        self.pb6.clicked.connect(lambda: self.addnum('6'))
        self.pb7.clicked.connect(lambda: self.addnum('7'))
        self.pb8.clicked.connect(lambda: self.addnum('8'))
        self.pb9.clicked.connect(lambda: self.addnum('9'))
        self.pbaplus.clicked.connect(lambda: self.addnum('+'))
        self.pbminus.clicked.connect(lambda: self.addnum('-'))
        self.pbtimes.clicked.connect(lambda: self.addnum('*'))
        self.pbdivide.clicked.connect(lambda: self.addnum('/'))
        self.pbdot.clicked.connect(lambda: self.addnum('.'))
        self.pbequal.clicked.connect(lambda: self.equal())
        self.AC.clicked.connect(lambda: self.clear())
        self.Delete.clicked.connect(lambda: self.deleteNum())

    def addnum(self, num):
        for i in self.result:
            if ord(num) >= 57 & ord(num) <= 48:
                self.SF = True
                break
            self.SF = False

        if self.result == '':
            self.output.clear()
            self.result += num
            self.output.setText(self.result)
        elif ord(self.result[-1:]) <= 57 & ord(self.result[-1:]) >= 48 & self.SF is False & self.RF is True & ord(num) >= 57 & ord(num) <= 48:
            self.output.clear()
            self.result += num
            self.output.setText(self.result)
            self.RF = False
        elif ord(self.result[-1:]) <= 57 & ord(self.result[-1:]) >= 48 & self.RF is False & ord(num) <= 57 & ord(num) >= 48:
            self.output.clear()
            self.result += num
            self.output.setText(self.result)
            self.RF = False
        elif ord(self.result[-1:]) >= 57 & ord(self.result[-1:]) <= 48 & self.SF is True & ord(num) >= 57 & ord(num) <= 48:
            self.result = self.result[:-1]
            self.output.setText(self.result)
            self.RF = False

    def equal(self):
        try:
            self.result = str(eval(self.result))
            self.output.setText(str(eval(self.result)))
            self.RF = True
        except SyntaxError:
            self.result = ''
            self.output.setText("你输了坨屎")
            self.RF = False
    def clear(self):
        self.result = ''
        self.output.clear()

    def deleteNum(self):
        self.result = self.result[:-1]
        self.output.setText(self.result)

if __name__ == "__main__":
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()
