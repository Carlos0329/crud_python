import os
import sqlite3
import smtplib


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "codeina.db")


def delete(correo):
    #se conecta a la base de datos
    con_bd = sqlite3.connect('codeina.db')
    #cursor a la db
    cursor_db = con_bd.cursor()
    #consultas
    sql = "DELETE FROM  usuarios WHERE correo=?"
    cursor_db.execute(sql, (correo,))
    con_bd.commit()
    #cierre del cursor
    cursor_db.close()
    if sql:
        return "Datos eliminados correctamente"
    else:
        return "Los datos no han sido eliminados, el correo no coincide"
