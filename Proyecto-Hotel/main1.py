import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel
from datetime import date, datetime

# Importa las clases de tu UI para cada ventana
from ui_enero import Ui_MainWindow as Ui_Enero
from ui_enero_habitacion import Ui_MainWindow as Ui_Habitacion

class CalendarioWidget(QMainWindow):
    def __init__(self, habitacion_widget):
        super().__init__()
        self.habitacion_widget = habitacion_widget
        self.ui = Ui_Enero()
        self.ui.setupUi(self)
        
        self.ui.pushButton_der.clicked.connect(self.siguiente_mes)
        self.ui.pushButton_izq.clicked.connect(self.anterior_mes)
        
        for i in range(1, 32):
            button = getattr(self.ui, f'pushButton_{i}', None)
            if button:
                button.clicked.connect(self.handle_day_click)

    def handle_day_click(self):
        sender = self.sender()
        if isinstance(sender, QPushButton):
            day = sender.text()
            print(f"Has clickeado el día: {day}")
            self.habitacion_widget.update_date(day)
            self.hide()
            self.habitacion_widget.show()

    def siguiente_mes(self):        
        self.hide()
        print("Mostrar siguiente mes")

    def anterior_mes(self):
        self.hide()
        print("Mostrar mes anterior")

class HabitacionWidget(QMainWindow):
    def __init__(self, calendario_widget):
        super().__init__()
        # Guarda la referencia a la ventana del calendario
        self.calendario_widget = calendario_widget
        self.ui = Ui_Habitacion()
        self.ui.setupUi(self)

        self.ui.pushButton_H101.clicked.connect(self.cambiar_color)
        
        # Conecta el nuevo botón de regreso
        # Asumo que tienes un botón llamado 'pushButton_regresar' en tu UI
        self.ui.pushButton_regresar = QPushButton("Regresar", self)
        self.ui.pushButton_regresar.clicked.connect(self.regresar_a_calendario)
        self.update_date(None)
    
    def update_date(self, day):
        dias_espanol = {
            "Monday": "Lunes", "Tuesday": "Martes", "Wednesday": "Miércoles",
            "Thursday": "Jueves", "Friday": "Viernes", "Saturday": "Sábado",
            "Sunday": "Domingo"
        }
        
        if day is not None:
            fecha_seleccionada = date(2026, 1, int(day))
            dia_semana_ingles = fecha_seleccionada.strftime("%A")
            dia_semana_espanol = dias_espanol.get(dia_semana_ingles, "")
            self.ui.label_16.setText(f"{dia_semana_espanol}")
            self.ui.label_16.setGeometry(1254, 160, 181, 51)
            self.ui.label_16.setStyleSheet("text-align: left; background-color: white; color:black;")
            self.ui.label_17.setText(f"{day}/01/2026")

        fecha_actual = datetime.now().date()
        dia_actual_formato = fecha_actual.strftime("%d/%m/%Y")
        self.ui.label_3.setText(f" Fecha: {dia_actual_formato}")

    def cambiar_color(self):
        self.ui.pushButton_H101.setStyleSheet("background-color: orange; color: white;")
        
    def regresar_a_calendario(self):
        self.hide() # Oculta la ventana actual
        self.calendario_widget.show() # Muestra la ventana del calendario
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    calendario_window = CalendarioWidget(None) # Inicialmente se crea sin la referencia
    habitacion_window = HabitacionWidget(calendario_window) # Se crea con la referencia al calendario
    
    # Se establece la referencia de la ventana de habitacion en la ventana de calendario
    calendario_window.habitacion_widget = habitacion_window

    calendario_window.show()
    
    sys.exit(app.exec())