import os
import sqlite3
import smtplib


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "codeina.db")


def bienvenida(correo):
    con_bd = sqlite3.connect('codeina.db')
    #cursor a la db
    cursor_db = con_bd.cursor()
    #consultas
    sql = "SELECT * FROM  usuarios WHERE correo=?"
    cursor_db.execute(sql, (correo,))
    fila = cursor_db.fetchone()
    correo=fila[0]
    clave=fila[1]
    nombre=fila[2]
    rol=fila[3]
    if rol ==1:
        rol="Administrador"
    elif rol==2:
        rol="Empleado"
    else:
        rol="Bodeguero"
    resultado=f"¡Bienvenido {nombre}!\nSu correo es: {correo} \nSu clave es : {clave} \nSu rol es : {rol}"
    return resultado
