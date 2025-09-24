import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel
from ui_enero_habitacion import Ui_MainWindow
from datetime import date, datetime

class MyWidget(QMainWindow):
    def __init__(self, day=""):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        dias_espanol = {
            "Monday": "Lunes",
            "Tuesday": "Martes",
            "Wednesday": "Miércoles",
            "Thursday": "Jueves",
            "Friday": "Viernes",
            "Saturday": "Sábado",
            "Sunday": "Domingo"
        }

        # Lógica para la fecha seleccionada del calendario
        if day.isdigit():
            fecha_seleccionada = date(2026, 1, int(day))
            dia_semana_ingles = fecha_seleccionada.strftime("%A")
            dia_semana_espanol = dias_espanol.get(dia_semana_ingles, "")

            # Actualiza las etiquetas con la fecha del calendario
            self.ui.label_16.setText(f"{dia_semana_espanol}")
            self.ui.label_17.setText(f"{day}/01/2026")
            
            self.ui.label_16.setStyleSheet("color:black; background-color: white; font: Javanese Text; font-size: 26px;")
            self.ui.label_17.setStyleSheet("color:black; background-color: white; font: Javanese Text; font-size: 20px;")
        
        # --- Etiqueta para la fecha actual (siempre visible) ---
        fecha_actual = datetime.now().date()
        dia_actual_formato = fecha_actual.strftime("%d/%m/%Y")
        
        # **CORRECCIÓN:** Se elimina la creación del QLabel, solo se actualiza el texto.
        self.ui.label_3.setText(f"     Fecha: {dia_actual_formato}")
        self.ui.label_3.setStyleSheet("color:black; background-color: #F2E8DB; font: Javanese Text; font-size: 26px; text-align: left;")

        self.ui.pushButton_H101.clicked.connect(self.cambiar_color)

    def cambiar_color(self):
        self.ui.pushButton_H101.setStyleSheet("background-color: orange; color: white;")
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    day_argument = ""
    if len(sys.argv) > 1:
        day_argument = sys.argv[1]
    
    window = MyWidget(day=day_argument)
    window.show()
    sys.exit(app.exec())