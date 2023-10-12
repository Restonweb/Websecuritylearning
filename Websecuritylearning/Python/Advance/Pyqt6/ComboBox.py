from PySide6.QtWidgets import QApplication, QWidget, QComboBox, QVBoxLayout
from PySide6.QtCore import Qt  # Flag Argument


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        cb = QComboBox()
        cb.addItems(['1','2','3'])

        cb.currentIndexChanged.connect(lambda :self.prc(cb.currentText()))

        mainlayout = QVBoxLayout()
        mainlayout.addWidget(cb)
        self.setLayout(mainlayout)

    def prc(self,x):
        print(x*2)
if __name__ == '__main__':
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()
