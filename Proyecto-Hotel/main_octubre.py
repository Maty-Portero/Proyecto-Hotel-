import sys, subprocess
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
from ui_octubre import Ui_MainWindow

class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton_der.clicked.connect(self.siguiente_mes)
        self.ui.pushButton_der.clicked.connect(self.anterior_mes)

        # Conectar todos los botones del 1 al 30 a la misma función
        for i in range(1, 32):
            button = getattr(self.ui, f'pushButton_{i}', None)
            if button:
                button.clicked.connect(self.handle_day_click)

    def handle_day_click(self):
        sender = self.sender() # Obtiene el objeto que emitió la señal
        if isinstance(sender, QPushButton):
            day = sender.text()
            print(f"Hiciste clic en el día: {day}")

    def siguiente_mes(self):
        self.close()
        subprocess.run(["python", 'main_noviembre.py'])

    def anterior_mes(self):
        self.close()
        subprocess.run(["python", 'main_septiembre.py'])
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWidget()
    window.show()
    sys.exit(app.exec())