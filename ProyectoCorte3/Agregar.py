import sys
import PyQt5.QtWidgets as PyQT
from PyQt5 import uic
import sqlite3


class Principal(PyQT.QMainWindow):
    def __init__(self): 
        super().__init__()
        self.initGui()
    
    def initGui(self):
        uic.loadUi("agregar.ui",self)
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
    app=PyQT.QApplication([])
    window= Principal()
    sys.exit(app.exec_())

if __name__=="__main__":
    main()