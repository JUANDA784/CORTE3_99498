import sqlite3
import re

def registrar(nombre, fechana, genero, intereses, descripcion, profesion, areadetrab):
    db = sqlite3.connect("BSEUSUARIOS.s3db")
    cursor = db.cursor()
    consulta = "INSERT INTO Registros (Nombre, fechana, genero, intereses, descripcion, profesion, areadetrab) VALUES (?, ?, ?, ?, ?, ?, ?)"
    cursor.execute(consulta, (nombre, fechana, genero, intereses, descripcion, profesion, areadetrab))
    db.commit()
    cursor.close()
    db.close()
    return "1"

def crearusu(email, contrasena, numcel):
    # Validar la contraseña
    if (
        len(contrasena) < 8 or len(contrasena) > 16 or
        not re.search(r"[A-Z]", contrasena) or
        not re.search(r"[a-z]", contrasena) or
        not re.search(r"\d", contrasena) or
        not re.search(r"[!@#$%^&*()\-_=+[{\]};:'\",<.>/?]", contrasena)
    ):
        return "La contraseña no cumple con los requisitos."

    db = sqlite3.connect("Bseusuarios.s3db")
    cursor = db.cursor()
    consulta = "INSERT INTO Creacionusuario (email, contrasena, numcel) VALUES (?, ?, ?)"
    cursor.execute(consulta, (email, contrasena, numcel))
    db.commit()
    cursor.close()
    db.close()
    return "1"

def validar(usuario):
    db = sqlite3.connect("Bseusuarios.s3db")
    db.row_factory = sqlite3.Row
    cursor = db.cursor()
    consulta = "SELECT contrasena FROM Creacionusuario WHERE email = ?"
    cursor.execute(consulta, (usuario,))
    resultado = cursor.fetchone()
    cursor.close()
    db.close()
    if resultado:
        return True, resultado["contrasena"]
    else:
        return False, None

def verificardatos(email, numcel):
    db = sqlite3.connect("Bseusuarios.s3db")
    db.row_factory = sqlite3.Row
    cursor = db.cursor()
    consulta = "SELECT * FROM Creacionusuario WHERE email = ? OR numcel = ?"
    cursor.execute(consulta, (email, numcel))
    resultado = cursor.fetchone()
    cursor.close()
    db.close()
    return resultado is not None

def main():
    Nombre = input('Ingrese su Nombre: ')
    fechana = int(input('Ingrese su fecha de nacimiento: '))
    genero = input('escoja su genero: ')
    intereses = input('Ingrese sus intereses: ')
    descripcion = input('Ingrese una descripcion de su persona: ')
    profesion = input('Ingrese su Profesion: ')
    areatrab = input('Ingrese su area de trabajo: ')
    registrar(Nombre, fechana, genero, intereses, descripcion, profesion, areatrab)
    x = input('\nIngrese su usuario: ')
    validar(x)


if __name__ == "__main__":
    main()