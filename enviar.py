import smtplib
from flask import Flask
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def enviarCorreo(correo,nombre,rol):
    #credenciales
        proveedor_correo = 'smtp.gmail.com: 587'
        remitente = 'codeinacorp@gmail.com'
        password = 'SenaCodeina'
        #conexion a servidor
        servidor = smtplib.SMTP(proveedor_correo)
        servidor.starttls()
        servidor.ehlo()
        #autenticacion
        servidor.login(remitente, password)

        if rol ==1:
            rol="Administrador"
        elif rol==2:
            rol="Cajero"
        else:
            rol="Bodeguero"
        #mensaje 
        mensaje = f'<h1>¡Bienvenido¡</h1><br><p>Hola {nombre}, te informamos que ahora eres parte de Codeina Corp</p><p>tu rol en la empresa es de {rol}</p><p>Bienvenido a tu nueva familia <a href="http://oferta.senasofiaplus.edu.co/sofia-oferta/">Link de prueba</a></p> '
        msg = MIMEMultipart()
        msg.attach(MIMEText(mensaje, 'html'))
        msg['From'] = remitente
        msg['To'] = correo
        msg['Subject'] = 'Confirmacion de registro'
        servidor.sendmail(msg['From'] , msg['To'], msg.as_string())