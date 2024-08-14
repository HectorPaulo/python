import mysql.connector
import smtplib
from email.mime.text import MIMEText
class Conexion:
    def __init__(self):
        self.name = None
        self.email = None
        self.password = None
    def correo_existente(self, email):
        # Función para verificar si el correo electrónico ya existe en la base de datos
        conexion = mysql.connector.connect(host="localhost", user="root", passwd="")
        cursor = conexion.cursor()
        cursor.execute("USE HARD;")
        cursor.execute("SELECT COUNT(*) FROM USUARIOS WHERE USUARIO_EMAIL = %s", (email,))
        count = cursor.fetchone()[0]
        conexion.close()
        return count > 0
    def validar_password(self, password):
        # Función para validar la contraseña
        conexion = mysql.connector.connect(host="localhost", user="root", passwd="")
        cursor = conexion.cursor()
        cursor.execute("USE HARD;")
        cursor.execute("SELECT COUNT(*) FROM USUARIOS WHERE USUARIO_PASSWORD = %s", (password,))
        count = cursor.fetchone()[0]
        conexion.close()
        return count > 0
    def ejecutar_consulta(self, name, email, password):
        self.miCorreo = "014417517@ulsaoaxaca.edu.mx"
        self.miPassword = "@salsaVERDE2702"
        self.name = name
        self.email = email
        self.password = password

        try:
            # Conexión a la base de datos
            conexion1 = mysql.connector.connect(host="localhost", user="root", passwd="", database="HARD")
            cursor1 = conexion1.cursor()

            # Insertar datos en la base de datos
            query = "INSERT INTO USUARIOS (USUARIO_NOMBRE, USUARIO_EMAIL, USUARIO_PASSWORD, USUARIO_TIPO) VALUES (%s, %s, %s, 'USUARIO')"
            cursor1.execute(query, (self.name, self.email, self.password))

            # Obtener todos los registros de usuarios (solo para fines de demostración)
            cursor1.execute("SELECT * FROM USUARIOS")
            rows = cursor1.fetchall()
            for row in rows:
                print(row)

            # Enviar correo electrónico
            mensaje = "Hola " + self.name + ",\n\n" + "Su correo electrónico ha sido registrado en HARD software con éxito. \n\n" + "Si no fue usted quien registró su correo electrónico, por favor contacte al administrador del sistema al siguiente número telefónico.\n\n" + "221 864 3652\n\n" + "Equipo de HARD"
            mime_message = MIMEText(mensaje, 'plain', 'utf-8')
            mime_message['From'] = self.miCorreo
            mime_message['To'] = self.email
            mime_message['Subject'] = "Registro exitoso en HARD software"
            
            emailConnection = smtplib.SMTP("smtp.office365.com", 587)
            emailConnection.starttls()
            emailConnection.login(self.miCorreo, self.miPassword)
            emailConnection.send_message(mime_message)
            emailConnection.quit()

            # Confirmar cambios y cerrar conexión
            conexion1.commit()
            cursor1.close()
            conexion1.close()

        except mysql.connector.Error as err:
            print("Error en la base de datos: ", err)

        except smtplib.SMTPException as smtp_err:
            print("Error al enviar el correo electrónico: ", smtp_err)