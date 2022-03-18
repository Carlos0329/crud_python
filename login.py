import os
import sqlite3
import smtplib
from bienvenida import bienvenida
from flask import Flask

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "codeina.db")

def login(correo, contrasena):
    #se conecta a la base de datos
    con_bd = sqlite3.connect('codeina.db')
    #cursor a la db
    cursor_db = con_bd.cursor()
    #consultass
    sql = "SELECT clave FROM  usuarios WHERE correo=?"
    cursor_db.execute(sql, (correo,))
    verificacion= cursor_db.fetchone()
    if verificacion is not None:
        if verificacion[0]==contrasena:
            return bienvenida(correo) 
        else : 
            return "La contraseña es incorrecta"
    else:
        return "El correo es incorrecto"