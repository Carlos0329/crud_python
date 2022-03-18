from login import login
from insertar import registro
from delete import delete
from actualizar import *
from flask import Flask

def index():
    opc=int(input("-----Bienvenido-----\n--Menu de opciones--\n-Seleccione 1 si desea logearse\n-Seleccione 2 si desea registrarse\n-Seleccione 3 si desea eliminar \n-Seleccione 4 si desea actualizar\n: "))
    if opc == 1:
        correo=input("Ingrese su correo: ")
        contrasena=input("Ingrese su contraseña: ")
        return login(correo,contrasena)

    elif opc == 2:
        correo = input("Ingrese su correo:     ")
        contrasena = input("Ingrese su contraseña: ")
        nombre = input("Ingrese su nombre:     ")
        rol = int(input("Ingrese el rol:        "))
        return registro(correo, contrasena, nombre, rol)

    elif opc == 3:
        correo=input("Ingrese el correo del usuario a eliminar: ")
        return delete(correo)
    elif opc == 4:
        correo = input("Ingrese el correo del cual actualizara los datos: ")
        validacion=validar(correo)
        if validacion==True:
            print("---Ingrese los datos para su actualizacion---")
            contrasena = input("Ingrese la nueva contraseña: ")
            nombre = input("Ingrese el nuevo nombre nombre: ")
            rol = int(input("Ingrese el nuevo rol: "))
            return update(contrasena, nombre, rol, correo)
        else :
            return print("El correo que ingresor No existe")
print(index())