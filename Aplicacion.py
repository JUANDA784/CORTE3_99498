import sys
import PyQt5.QtWidgets as PyQT
from PyQt5 import uic


class Principal(PyQT.QMainWindow):
    def __init__(self): 
        super().__init__()
        self.initGui()
    
    def initGui(self):
        uic.loadUi("Practicainterfaz.ui",self)
        self.show()
        
        self.pushButton.clicked.connect(lambda: self.calcular())

    def calcular(self):
        texto1 = self.num1.text()
        texto2 = self.num2.text()
        sum = float(texto1)+float(texto2)
        rest = float(texto1)-float(texto2)
        mult = float(texto1)*float(texto2)
        div = float(texto1)/float(texto2)

        if  self.sumar.isChecked()==True:
            self.result.setText(str(sum))
        elif  self.restar.isChecked()==True:
            self.result.setText(str(rest))
        elif  self.mult.isChecked()==True:
            self.result.setText(str(mult))
        else:
            self.result.setText(str(div))

def main():
    app=PyQT.QApplication([])
    window= Principal()
    sys.exit(app.exec_())

if __name__=="__main__":
    main()