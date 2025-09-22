import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
from ui_septiembre import Ui_MainWindow

class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Conectar todos los botones del 1 al 30 a la misma función
        for i in range(1, 31):
            button = getattr(self.ui, f'pushButton_{i}', None)
            if button:
                button.clicked.connect(self.handle_day_click)

    def handle_day_click(self):
        sender = self.sender() # Obtiene el objeto que emitió la señal
        if isinstance(sender, QPushButton):
            day = sender.text()
            print(f"Hiciste clic en el día: {day}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWidget()
    window.show()
    sys.exit(app.exec())