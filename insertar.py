import os
import sqlite3
import smtplib
from enviar import enviarCorreo


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "codeina.db")

def registro(correo, contrasena, nombre, rol):
    #se conecta a la base de datos
    con_bd = sqlite3.connect('codeina.db')
    #cursor a la db
    cursor_db = con_bd.cursor()
    #consultas
    sql = "INSERT INTO usuarios (Correo,Clave,Nombre,Rol) VALUES (?,?,?,?)"
    #ejecuta la consulta
    sql2=cursor_db.execute(sql, (correo, contrasena,nombre,rol))
    con_bd.commit()
    #cierre del cursor
    cursor_db.close()
    if sql2:
        enviarCorreo(correo,nombre,rol)
        return "Registro exitoso"
    else:
        return "Registro fallido"
