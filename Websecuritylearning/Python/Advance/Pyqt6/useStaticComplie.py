from PySide6.QtWidgets import QApplication, QWidget
from login import Ui_widget
class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.ui  = Ui_widget()
        self.ui.setupUi(self)
if __name__ == '__main__':
    app =  QApplication([])
    window = MyWindow()
    window.show()
    app.exec()