from operator import truediv
import os
import sqlite3
import smtplib


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "codeina.db")


def validar(correo):
    con_bd = sqlite3.connect('codeina.db')
    #cursor a la db
    cursor_db = con_bd.cursor()
    #consultas
    sql = "SELECT Correo FROM usuarios WHERE Correo=?"
    cursor_db.execute(sql, (correo,))
    verificacion= cursor_db.fetchone()
    #cierre del cursor
    if verificacion is not None:
        print("entro aca")
        return True
    else:
        return False

    
def update(contrasena,nombre,rol,correo):
    #se conecta a la base de datos
    con_bd = sqlite3.connect('codeina.db')
    #cursor a la db
    cursor_db = con_bd.cursor()
    #consultas
    sql = "UPDATE usuarios  SET clave=?, nombre=?, rol=? WHERE correo=?"
    cursor_db.execute(sql, (contrasena, nombre,rol,correo,))
    con_bd.commit()
    #cierre del cursor
    cursor_db.close()
    if sql:
        return "Datos actualizados correctamente"
    else:
        return "Los datos no se han actualizado"
