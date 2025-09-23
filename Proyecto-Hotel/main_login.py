import sys, subprocess
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
from ui_login import Ui_MainWindow

class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

    # Conecta el botón 'Iniciar sesión' a una función
        self.ui.pushButton_1.clicked.connect(self.iniciar_sesion)

    def iniciar_sesion(self):
        # Esta es la función que se ejecutará cuando el botón sea clickeado
        usuario = self.ui.lineEdit.text()
        contrasena = self.ui.lineEdit_2.text()
        print(f"Intento de inicio de sesión - Usuario: {usuario}, Contraseña: {contrasena}")
        # Aquí puedes agregar la lógica de validación o conexión a base de datos.
        # 1. Cierra la ventana actual
        self.close()

        # 2. Abre la nueva ventana usando subprocess
        # Asegúrate de que "nombre_del_script_de_la_otra_ventana.py"
        # sea el nombre correcto del archivo de la otra ventana
        subprocess.run(["python", "main_enero.py"])


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWidget()
    window.show()
    sys.exit(app.exec())