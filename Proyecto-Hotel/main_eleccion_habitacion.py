import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
from ui_eleccion_habitacion import Ui_MainWindow

class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWidget()
    window.show()
    sys.exit(app.exec())