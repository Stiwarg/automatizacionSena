#Este Bot realizo dos envios, el primero a inicios del trimestre y el otro faltando 15 para finalizar el trimestre 
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from datetime import datetime, timedelta
from apscheduler.schedulers.background import BackgroundScheduler
import schedule
import time
import mysql.connector

#Configuracion del servidor SMTP y credenciales

smtp_server = 'smtp.gmail.com'
smtp_port = 587 # Este es puerto de GMAIL para SMTP
smtp_username = 'stiwarg798@gmail.com'
smtp_password = 'rttpwprpmsfyjsbv'


def connect_to_database():
        # Establecer conexión con la base de datos
    try:
        connection = mysql.connector.connect(
            host="127.0.0.1",
            port=3306,
            user="root",
            password="",
            database="prueba"
        )
        return connection
    except mysql.connector.Error as error:
        print("Error al conectar a la base de datos: ", error)
        return None

#Funcion para enviar el correo electronico
def enviar_correo(contexto=None):

    connection = connect_to_database()
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

        query_trimester = "SELECT id as id_trimestre FROM fechas_trimestre WHERE fecha_inicio <= NOW() AND fecha_fin >= NOW()"
        cursor.execute(query_trimester)
        trimester_result = cursor.fetchone()

        if trimester_result:
            id_trimester = trimester_result[0]
        else:
            print("No se encontró ningún trimestre activo.")
            return
        #Consulta 
        # los resultados de aprendizaje para cada instructor 
        query_results = f"SELECT CONCAT_WS(' ', i.nombre, i.apellidos) AS nombre_completo, r.resultado AS resultado_aprendizaje,actividad_proyecto,trimestre_curso, curso, numero_ficha FROM resultados_asignados r INNER JOIN instructores i ON r.instructor_responsable = i.id WHERE r.instructor_responsable = {id_instructor} AND r.trimestres_id = {id_trimester}"

        cursor.execute(query_results)
        instructors = cursor.fetchall()

        # Genera el HTML para la tabla de resultados de aprendizaje para cada instructor.
        html_tabla = "<table border='1'><tr><th>Nombre del Instructor</th><th>Resultado de Aprendizaje</th><th>Actividad del Proyecto</th><th>Trimestre del Curso</th><th>Nombre del Curso</th><th>Numero de Ficha</th></tr>"
        for resultado in instructors:
            html_tabla += f"<tr><td>{resultado[0]}</td><td>{resultado[1]}</td><td>{resultado[2]}</td><td>{resultado[3]}</td><td>{resultado[4]}</td><td>{resultado[5]}</td></tr>"
        html_tabla += "</table>"

        #Configuracion del correo
        sender_email = 'stiwarg798@gmail.com'

        #Aqui se puede decidir cambiar el asunto o el cuerpo del mensaje basado en el contexto
        if contexto == 'inicio':
            subject = 'Inicio del Trimestre - Recordatorio de los resultados de aprendizaje a evaluar'
            #Consulta para obtener la informacion de la primer plantilla que se va mandar
            query_body = "SELECT informacion FROM plantilla_correos WHERE ID = 1"
            cursor.execute(query_body)
            body_info = cursor.fetchone()[0]
        elif contexto == 'fin-15':
            subject = 'Fin del Trimestre - Últimos 15 días para evaluar resultados de aprendizaje'
            #Consulta para obtener la informacion de la primer plantilla que se va mandar
            query_body = "SELECT informacion FROM plantilla_correos WHERE ID = 2"
            cursor.execute(query_body)
            body_info = cursor.fetchone()[0]
        else:
            subject = 'Recordatorio de los resultados de aprendizaje a evaluar'
            body_info = " "

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
        image_files = ['bots/img/sena.png','bots/img/redes1.png','bots/img/redes2.png','bots/img/redes3.png','bots/img/redes4.png','bots/img/redes5.png','bots/img/redes6.png','bots/img/redes7.png']

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

def search_date_trimester():
    # Establecer conexión con la base de datos
    connection = connect_to_database()
    cursor = connection.cursor()
    
    # Consulta para obtener la fecha de inicio y fin del trimestre actual
    query_date_trimester = "SELECT fecha_inicio, fecha_fin FROM fechas_trimestre WHERE fecha_inicio <= NOW() AND fecha_fin >= NOW()"
    cursor.execute(query_date_trimester)
    
    # Obtener el resultado de la consulta
    result_date = cursor.fetchone()
    
    # Cerrar el cursor y la conexión con la base de datos
    cursor.close()
    connection.close()

    # Verificar si se encontró la fecha del trimestre actual
    if result_date:
        # Obtener la fecha de inicio y fin del trimestre del resultado
        fecha_inicio, fecha_fin = result_date
        
        # Ajustar la hora de inicio a las 8:00 AM
        fecha_inicio_con_hora = datetime(fecha_inicio.year, fecha_inicio.month, fecha_inicio.day, 20, 12, 0)
        
        # Obtener la fecha fin menos 15 días
        fecha_fin_con_hora = datetime(fecha_fin.year, fecha_fin.month, fecha_fin.day, 20, 12, 0) - timedelta(days=15)

        return fecha_inicio_con_hora, fecha_fin_con_hora

def calculate_start_date_next_trimester():
    # Establecer conexión con la base de datos
    connection = connect_to_database()
    cursor = connection.cursor()
    
    # Consulta para obtener la fecha de inicio y fin del próximo trimestre
    query_next_trimester = "SELECT fecha_inicio, fecha_fin FROM fechas_trimestre WHERE fecha_inicio > NOW() ORDER BY fecha_inicio ASC LIMIT 1"
    cursor.execute(query_next_trimester)
    
    # Obtener el resultado de la consulta
    result_next_trimester = cursor.fetchone()
    
    # Cerrar el cursor y la conexión con la base de datos
    cursor.close()
    connection.close()

    # Verificar si se encontró la fecha de inicio del próximo trimestre
    if result_next_trimester:
        # Obtener la fecha de inicio del próximo trimestre del resultado
        fecha_inicio_proximo_trimestre = result_next_trimester[0]
        return fecha_inicio_proximo_trimestre
    else:
        # Imprimir un mensaje de error si no se encontró la fecha de inicio del próximo trimestre
        print("No se encontraron fecha de inicio para el próximo trimestre.")
        return None

def program_shipments():
    # Crear un objeto scheduler de BackgroundScheduler
    scheduler = BackgroundScheduler()

    # Obtener las fechas del trimestre actual y 15 días antes del final del trimestre
    fecha_inicio, fecha_fin_menos_15 = search_date_trimester()

    # Verificar si se encontraron las fechas del trimestre actual y de envío de 15 días antes del final
    if fecha_inicio and fecha_fin_menos_15:
 
        # Programar el envío de correo para el inicio del trimestre
        scheduler.add_job(enviar_correo, 'date', run_date=fecha_inicio, args=['inicio'])

        # Programar el envío de correo para 15 días antes del final del trimestre
        scheduler.add_job(enviar_correo, 'date', run_date=fecha_fin_menos_15, args=['fin-15'])

        # Obtener la fecha de inicio del próximo trimestre
        date_start_next_trimester = calculate_start_date_next_trimester()

        # Programar la ejecución de program_shipments() para la fecha de inicio del próximo trimestre
        scheduler.add_job(program_shipments, 'date', run_date=date_start_next_trimester)

        # Iniciar el scheduler
        scheduler.start()

# Programar el envio del correo una vez al mes durante tres meses
program_shipments()

# Mantener el programa en ejecución
while True:
    pass
