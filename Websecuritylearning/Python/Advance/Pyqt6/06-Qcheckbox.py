from PySide6.QtWidgets import QApplication, QWidget, QCheckBox, QVBoxLayout
from PySide6.QtCore import Qt  # Flag Argument


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        cb = QCheckBox("Option")
        cb.stateChanged.connect(self.prc)
        mainlayout = QVBoxLayout()
        mainlayout.addWidget(cb)
        self.setLayout(mainlayout)

    def prc(self, x):
        print(x)


if __name__ == '__main__':
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()
