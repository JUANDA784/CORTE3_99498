# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5 import QtWidgets
from PyQt5.uic import loadUi
import consultarbase as cb
import sys
from Agregar import MostrarPerfil


class Principal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = loadUi("loginInterfaz.ui", self)
        self.show()

        self.ui.entrar.clicked.connect(self.entrando)
        self.ui.llevarsingup.clicked.connect(self.opensingup)

        self.show_password = False  # Variable para almacenar el estado de visualización de la contraseña

        self.ui.vercontra.clicked.connect(self.verlacontrasena)  # Conecta la señal del botón con la función
        

    def verlacontrasena(self):
        self.show_password = not self.show_password  # Cambia el estado de visualización de la contraseña

        if self.show_password:
            self.ui.contrasena_log.setEchoMode(QtWidgets.QLineEdit.Normal)  # Muestra el texto normalmente
        else:
            self.ui.contrasena_log.setEchoMode(QtWidgets.QLineEdit.Password)

    def entrando(self):
        usuario = self.ui.usuario_log.text()
        contrasena = self.ui.contrasena_log.text()
        res, contrasenaveri = cb.validar(usuario)
        if res and contrasena == contrasenaveri:
            QMessageBox.information(self, "Inicio de sesión", "Inicio de sesión exitoso")
        else:
            QMessageBox.warning(self, "Inicio de sesión", "Nombre de usuario o contraseña incorrectos")

    def opensingup(self):
        self.hide()  # Ocultar la ventana de loginInterfaz.ui
        singup_window = SingUpWindow()
        singup_window.show()

class SingUpWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = loadUi("singup.ui", self)
        self.show()

        self.ui.registrar.clicked.connect(self.registroexitoso)

    def registroexitoso(self):
        email = self.ui.inemail.text()
        contrasena = self.ui.incontrasena.text()
        numcel = self.ui.innumcel.text()

        if cb.verificardatos(email, numcel):
            QMessageBox.warning(self, "Registro", "El correo electrónico o número de celular ya está registrado.")
        else:
            resultado = cb.crearusu(email, contrasena, numcel)
            QMessageBox.information(self, "Registro", "Registro exitoso.")
            self.hide()  # Ocultar la ventana de singup.ui
            create_user_window = CreateUserWindow()
            create_user_window.show()

class CreateUserWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = loadUi("createuser.ui", self)
        self.show()

        self.ui.crear.clicked.connect(self.registro)

    def registro(self):
        nombre = self.ui.innombre.text()
        fechana = self.ui.innacimiento.text()

        if self.ui.women.isChecked():
            genero = 'femenino'
        else:
            genero = 'masculino'

        intereses = self.ui.inintereses.text()
        descripcion = self.ui.indescripcion.text()
        profesion = self.ui.inprofesiones.text()
        areadetrab = self.ui.inworkarea.text()

        result = cb.registrar(nombre, fechana, genero, intereses, descripcion, profesion, areadetrab)
        if result == "1":
            QMessageBox.information(self, "Registro", "Usuario creado exitosamente")
            self.hide()  # Ocultar la ventana de createuser.ui
            login_window = MostrarPerfil()  # Crear una instancia de la clase Principal
            login_window.show()  # Mostrar la ventana de loginInterfaz.ui

            ultimo_perfil = login_window.get_ultimo_perfil()
            
        else:
            QMessageBox.warning(self, "Registro", "Error al crear el usuario")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Principal()
    sys.exit(app.exec_())


