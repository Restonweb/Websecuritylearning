from PySide6.QtWidgets import QApplication, QMainWindow, QLineEdit
from PySide6.QtCore import Qt    #Flag Argument
from login import Ui_widget
class MyWindow(QMainWindow,Ui_widget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton.clicked.connect(self.loginFuc)

    def loginFuc(self):
        account = self.lineEdit.text()
        password = self.lineEdit_3.text()
        if (account == "redcamellia") & (password == "123"):
            print("hello？")
        else:
            print("Nope.")

if __name__ == '__main__':
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()