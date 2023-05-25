import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QHeaderView 
from PyQt5.QtCore import QPoint, QPropertyAnimation, QEasingCurve
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.uic import loadUi
import sqlite3


class Principal(QMainWindow):
    def __init__(self): 
        super(Principal, self).__init__()
        loadUi('interfazdinamica.ui',self)

        self.conexion = sqlite3.connect('Bseusuarios.s3db')

        self.show()

        # Barra de titulo
        self.click_posicion = QPoint()
        #self.bt_perfil.clicked.connect(self.abrir_pestaña_superior)
        #self.bt_inicio.clicked.connect(self.volver_al_inicio)
#
        ## Botones
        #self.bt_mas.clicked.connect(self.abrir_pestaña_busqueda)
        #self.bt_search.clicked.connect(self.busqueda)
        #self.bt_actualizar.clicked.connect(self.refrescar)
        #self.bt_agregar.clicked.connect(self.agregar_amigos)
        #self.bt_amigos.clicked.connect(self.ver_perfiles)
#
        ## Coneccion botones
        #self.bt_mas.clicked.connect(lambda: self.stackedWiget.setCurrentWidget(self.page_agregar))
        #self.bt_inicio.clicked.connect(lambda: self.stackedWiget.setCurrentWidget(self.page_perfil))
        self.bt_menu.clicked.connect(lambda: self.frame_menu.expandMenu())

        # Metodo para mover el menu lateral izquiedo
    #def mover_menu(self):
    #    if True:
    #        width = self.frame_menu.width()
    #        normal = 0
    #        if width == 0:
    #            extender = 200
    #        else:
    #            extender = normal
    #        self.animacion.QPropertyAnimation(self.frame_menu, b'minimumWidth')
    #        self.animacion.setDuration(300)
    #        self.animacion.setStartValue(width)
    #        self.animacion.setEndValue(extender)
    #        self.animacion.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
    #        self.animacion.start()
#
    #def search_datos(self):
    #    Profesion_a_buscar = self.buscar_profesion.text()
    #    #Obtener datos SQLite3
    #    cursor = self.conexion.cursor()
    #    cursor.execute("SELECT profesion, nombre, areatrab WHERE Datos = '{}' ".format(Profesion_a_buscar))
    #    profesiones = cursor.fetchall()
    #    cursor.close()
    #    if profesiones:
    #        self.profesion.setText(profesiones[0][1])
    #        self.nombre.setText(profesiones[0][2])
    #        self.areatrab.setText(profesiones[0][2])
#






    #def buscador(self):
    #    uic.loadUi("busquedaamigos.ui",self)
    #    self.show()
#
    #    db = sqlite3.connect("Bseusuarios.s3db")
    #    db.row_factory=sqlite3.Row
    #    cursor=db.cursor()
    #    consulta="select * from Personas WHERE profesion = '" + profesion +"'"
    #    cursor.execute(consulta)
    #    resultado=cursor.fetchone()
    #    print(list(resultado))
    #    cursor.close()
    #    db.close()
    #    return resultado
    #
    #def agregar(self):
    #    db = sqlite3.connect("Bseusuarios.s3db")
    #    db.row_factory = sqlite3.Row
    #    cursor = db.cursor()
    #    consulta = "insert into Personas values ('"+ profesion +"','" + nombre + "'," + str(edad) +","+str(documento)+",'"perfil"')"
    #    cursor.execute(consulta)
    #    db.commit()
    #    cursor.close()
    #    db.close()
    #    return "1"
#
    #def abrir(self):
    #    Vista()
    #    self.close()


def main():
    app = QApplication(sys.argv)
    my_app = Principal()
    my_app.show()
    sys.exit(app.exec_())
    
if __name__=="__main__":
    main()