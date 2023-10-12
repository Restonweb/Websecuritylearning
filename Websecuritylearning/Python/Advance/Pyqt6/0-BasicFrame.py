from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtCore import Qt    #Flag Argument

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()


if __name__ == '__main__':
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()


# from PySide6.QtWidgets import QPushButton
# btn = QPushButton("我是按钮", self)
# btn.setGeometry(0,0,200,100)
# btn.setToolTip("这是个按钮")
# btn.setText("按钮？")

# from PySide6.QtWidgets import QLabel
# lb = QLabel("我是个标签",self)
# lb.setText("shift！")
# lb.setAlignment(Qt.AlignmentFlag.AlignCenter)

# from PySide6.QtWidgets import QLineEdit
# le = QLineEdit(self)
#         le.setPlaceholderText("请输入内容")