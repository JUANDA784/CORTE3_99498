import sqlite3
def Registrar(Nombre, Apellido, Edad, Documento):
    db = sqlite3.connect("JUANUSB.s3db")
    db.row_factory = sqlite3.Row
    cursor = db,cursor()
    consulta = "insert into Persona (Nombre, Apellido, Edad, Documento.) values ('"+ Nombre +"','"+ Apellido +"'," + str(Edad) +")"

def main():

if __name__=='__main__':
    main()