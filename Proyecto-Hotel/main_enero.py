import sys, subprocess
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
from ui_enero import Ui_MainWindow

class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.month_name = "enero"
        
        self.ui.pushButton_der.clicked.connect(self.siguiente_mes)
        self.ui.pushButton_izq.clicked.connect(self.anterior_mes)
        

        # Conectar todos los botones del 1 al 30 a la misma función
        for i in range(1, 32):
            button = getattr(self.ui, f'pushButton_{i}', None)
            if button:
                button.clicked.connect(self.handle_day_click)

    def handle_day_click(self):
        sender = self.sender()
        if isinstance(sender, QPushButton):
            day = sender.text()
            print(f"Has clickeado el día: {day}")

            self.close()
            # **MODIFICACIÓN AQUÍ**: Pasa el día y el mes como argumentos
            subprocess.run(["python", "main_enero_habitacion.py", day, self.month_name])
            
    #def 

    def siguiente_mes(self):        
        self.close()
        subprocess.run(["python", "main_febrero.py"])

    def anterior_mes(self):
        self.close()
        subprocess.run(["python", "main_diciembre.py"])

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWidget()
    window.show()
    sys.exit(app.exec())