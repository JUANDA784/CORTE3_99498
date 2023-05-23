import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QHeaderView 
from PyQt5.QtCore import QPropertyAnimation, QEasingCurve
from PyQt5 import QtCore, QtWidgets
from PyQt5.uic import loadUi
import sqlite3


class Principal(QMainWindow):
    def __init__(self): 
        super().__init__()
        loadUi('dinamica.ui',self)

        # Barra de titulo
        self.bt_menu.clicked.connect(self.mover_menu)
        self.bt_perfil.clicked.connect(self.abrir_pestaña_superior)
        self.bt_inicio.clicked.connect(self.volver_al_inicio)

        # Botones
        self.bt_mas.clicked.connect(self.abrir_pestaña_busqueda)
        self.bt_search.clicked.connect(self.busqueda)
        self.bt_actualizar.clicked.connect(self.refrescar)
        self.bt_agregar.clicked.connect(self.agregar_amigos)
        self.bt_amigos.clicked.connect(self.ver_perfiles)

        # Coneccion botones
        self.bt_mas.clicked.connect(lambda: self.stackedWiget.setCurrentWidget(self.page_agregar))
        self.bt_inicio.clicked.connect(lambda: self.stackedWiget.setCurrentWidget(self.page_perfil))



    def initGui(self):
        uic.loadUi("dinamica.ui",self)
        self.show()
        
        self.mas.clicked.connect(lambda: self.buscador())

    def buscador(self):
        uic.loadUi("busquedaamigos.ui",self)
        self.show()

        db = sqlite3.connect("Bseusuarios.s3db")
        db.row_factory=sqlite3.Row
        cursor=db.cursor()
        consulta="select * from Personas WHERE profesion = '" + profesion +"'"
        cursor.execute(consulta)
        resultado=cursor.fetchone()
        print(list(resultado))
        cursor.close()
        db.close()
        return resultado
    
    def agregar(self):
        db = sqlite3.connect("Bseusuarios.s3db")
        db.row_factory = sqlite3.Row
        cursor = db.cursor()
        consulta = "insert into Personas values ('"+ profesion +"','" + nombre + "'," + str(edad) +","+str(documento)+",'"perfil"')"
        cursor.execute(consulta)
        db.commit()
        cursor.close()
        db.close()
        return "1"

    def abrir(self):
        Vista()
        self.close()


def main():
    app = QApplication([])
    window = Principal()
    sys.exit(app.exec_())

if __name__=="__main__":
    main()