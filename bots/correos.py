#Este bot es de pruebas 
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import schedule
import time
import mysql.connector

#Configuracion del servidor SMTP y credenciales

smtp_server = 'smtp.gmail.com'
smtp_port = 587 # Este es puerto de GMAIL para SMTP
smtp_username = 'stiwarg798@gmail.com'
smtp_password = 'rttpwprpmsfyjsbv'

#Funcion para enviar el correo electronico
def enviar_correo():

    #Conexion a la base de datos para obtener destinatariios

    connection = mysql.connector.connect(
        host='127.0.0.1',
        port= 3307,
        user='root',
        password='',
        database='prueba'
    )

    cursor = connection.cursor()

    #Consulta para obtener destinatarios de la base de datos
    query_correo = "SELECT id, nombre ,correo FROM instructores"
    cursor.execute(query_correo)
    recipients = cursor.fetchall()  # Esto debería devolver una lista de tuplas

    # Se itera sobre cada instructor

    for instructor in recipients:
        id_instructor = instructor[0]
        name_instructor = instructor[1]
        email_instructor = instructor[2]

        #Consulta los resultados de aprendizaje para cada instructor 
        query_results = f"SELECT CONCAT_WS(' ', i.nombre, i.apellidos) AS nombre_completo, r.resultado FROM resultados_asignados r INNER JOIN instructores i ON r.instructores_id = i.id WHERE r.instructores_id = {id_instructor}"

        cursor.execute(query_results)
        instructors = cursor.fetchall()

        # Genera el HTML para la tabla de resultados de aprendizaje para cada instructor.
        html_tabla = "<table border='1'><tr><th>Nombre del Instructor</th><th>Resultado de Aprendizaje</th></tr>"
        for resultado in instructors:
            html_tabla += f"<tr><td>{resultado[0]}</td><td>{resultado[1]}</td></tr>"
        html_tabla += "</table>"

        #Consulta para obtener la informacion de la primer plantilla que se va mandar
        query_body = "SELECT informacion FROM plantilla_correos WHERE ID = 1"
        cursor.execute(query_body)
        body_info = cursor.fetchone()[0]

        #Configuracion del correo
        sender_email = 'stiwarg798@gmail.com'
        subject = 'Recordatorio de los resultados de aprendizajes a evaluar'

        #Se crea objeto MIMEMultipart 
        message = MIMEMultipart()
        message['From'] = sender_email
        message['To'] = email_instructor
        message['Subject'] = subject

        html_content = """
        <html>
                <head>
                    <link rel="preconnect" href="https://fonts.googleapis.com">
                    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
                    <link href="https://fonts.googleapis.com/css2?family=Libre+Baskerville:ital,wght@0,400;0,700;1,400&display=swap" rel="stylesheet">
                    <link href="https://db.onlinewebfonts.com/c/9a176c4742d916a8351e208f0e3d9c30?family=LTC+Village+No+2+SC+W00+SC" rel="stylesheet">
                    <style>
                        p {
                            margin: 0; /* Añadido para resetear los márgenes */
                            padding: 0; /* Añadido para resetear los rellenos */
                        }
                    </style>
                </head>
                <body style="color: rgb(102, 102, 102);">
                    <table width="100%" border="0" style="text-align: left;">
                        <tr>
                            <td width="20%" style="border-right: none; text-align: center; vertical-align: middle; position:relative; padding-top:50px;">
                                <img src="cid:img1">
                            </td>
                            <td>
                                <div style="height: 120px; border-left: 1px solid #ccc;"></div>
                            </td>            
                            <td width="79%" style="position: relative;">
                                <p style="font-family: 'Libre Baskerville', serif; font-size: 19px; color: rgb(106, 168, 79); margin-bottom:0px; margin-top:50px;"><strong>Juan Gonzalo Alvarez Diaz</strong></p>
                                <p style="font-family: 'LTC Village No 2 SC', sans-serif; font-size: 12px; color: rgb(102, 102, 102); margin-bottom:0px;"><em>Centro De Electricidad Y Automatización Industrial - <br> Instructor G20</em><br>
                                    <a href="mailto:jgalvarez@sena.edu.co">jgalvarez@sena.edu.co</a><br>PBX: +(57) 601 5461500 Ext:<br>Calle 52 No. 2 Bis 15</p>
                                <!-- Agrega enlaces a las redes sociales aquí -->
                                <div style="display:flex; padding-left: 0px; margin-top: 20px; margin-bottom:0; position:relative;">
                                    <a href="https://www.instagram.com/senacomunica/?hl=es-la"><img src="cid:img6" style="margin-right: 10px; "></a>
                                    <a href="https://web.facebook.com/SENA?_rdc=1&_rdr"><img src="cid:img5" style="margin-right: 10px;"></a>
                                    <a href="https://twitter.com/SENAComunica"><img src="cid:img4" style="margin-right: 10px;"></a>
                                    <a href="https://www.youtube.com/user/SENATV"><img src="cid:img3" style="margin-right: 10px;"></a>
                                    <a href="https://www.linkedin.com/school/servicio-nacional-de-aprendizaje-sena-/"><img src="cid:img2" style="margin-right: 10px;"></a>
                                    <a href="https://www.sena.edu.co/es-co/Paginas/default.aspx"><img src="cid:img7" style="padding-top: 15px"></a>
                                </div>
                            </td>
                        </tr>
                        <tr>
                            <td colspan="3" width="69%" style="position: relative;">
                                <div style="display:flex; padding-left: 200px; position:relative; bottom:5px;">
                                    <img src="cid:img8" style="width:120px; height:13px;">
                                    <br>  
                                </div>
                            </td>
                        </tr>
                    </table>
                </body>
                </html>
            """
        # Adjuntar cuerpo del mensaje
        message.attach(MIMEText(body_info + " <br> " + html_tabla + " <br> " + html_content, 'html'))

        # Adjuntar imagenes
        image_files = ['img/sena.png','img/redes1.png','img/redes2.png','img/redes3.png','img/redes4.png','img/redes5.png','img/redes6.png','img/redes7.png']

    # Adjuntar imágenes al mensaje
        for idx, image_path in enumerate(image_files, start=1):
            with open(image_path, 'rb') as file:
                img = MIMEImage(file.read())
                img.add_header('Content-ID', f'<img{idx}>')  # Asigna un identificador único a cada imagen
                message.attach(img)

        # Iniciar conexion SMTP Y enviar correo 
        with smtplib.SMTP(smtp_server, smtp_port) as server:

            server.starttls()
            server.login(smtp_username, smtp_password)
            server.sendmail(sender_email, [email_instructor] , message.as_string())
            print('Correo enviado con exito.')

    cursor.close()
    connection.close()


# Programar el envio del correo una vez al mes durante tres meses
enviar_correo()

# Un ciclo para ejecutar la programacion 
while True:
    schedule.run_pending()
    time.sleep(1)
