from PySide6.QtWidgets import QApplication, QMainWindow, QLineEdit
from PySide6.QtCore import Qt    #Flag Argument

# import QPushButton
# btn = QPushButton("我是按钮", self)
# btn.setGeometry(0,0,200,100)
# btn.setToolTip("这是个按钮")
# btn.setText("按钮？")

# import QLabel
# lb = QLabel("我是个标签",self)
# lb.setText("shift！")
# lb.setAlignment(Qt.AlignmentFlag.AlignCenter)


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        le = QLineEdit(self)
        le.setPlaceholderText("请输入内容")

if __name__ == '__main__':
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()