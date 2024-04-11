#Se importa las bibliotecas necesarias de Selenium y Time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select 
from datetime import datetime, timedelta
from selenium.webdriver.common.keys import Keys
import mysql.connector


def run_code():

    #Se define la carperta donde se va a descargar los archivos:
    download_folder = "C:\\Users\\SENA\\Desktop\\bot\\bots\\documentos"

    #Configurar las opciones de chrome 
    chrome_options = Options()
    chrome_options.add_experimental_option("prefs",{
        "download.default_directory": download_folder,
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing.enabled": True
    })

    #Se crea un servicio de Chrome Webdriver y se inicia el navegador Chrome con las opciones 
    service = Service(executable_path=r"C:\dchrome\chromedriver.exe")
    driver = webdriver.Chrome(service=service, options=chrome_options)

    #Se navega a la pagina web
    driver.get("https://appsceai.com/Saf/usuarios/login")

    input_document = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, 'UsuarioDocumento')))
    input_document.send_keys("75077923")

    input_password = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, 'UsuarioClave')))
    input_password.send_keys("Futuro2022")

    # Esperar a que aparezca el elemento div con la clase "submit"
    div_element = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, '//div[@class="submit"]'))
    )

    # Acceder al elemento input dentro del div
    btn_sign_in = div_element.find_element(By.XPATH, './/input[@class="btn btn-primary"]')
    btn_sign_in.click()

    combox_reportes = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, './/i[@class="fa fa-download"]')))
    combox_reportes.click()

    ul_reportes = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '//ul[@class="treeview-menu menu-open"]')))
    asignacion_resultados = ul_reportes.find_element(By.XPATH, './/a[contains(text(), "Asignacion de resultados")]')

    asignacion_resultados.click()

    # Obtener la fecha actual
    present_date = datetime.now()

    select_trimestres = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.ID, 's2id_TrimestreTrimestres')))
    select_trimestres.click()

    # Esperar a que aparezcan las opciones en la lista desplegable
    options_list = WebDriverWait(driver, 60).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "select2-results"))
    )

    # Obtener todas las opciones
    options = options_list.find_elements(By.XPATH, './/li[@role="presentation"]')

    # Calcular la fecha más cercana
    closest_date_option = None

    #Esta linea almacenara la diferencia de dias mas pequeña encontrada hasta el momento
    #Se inicializa como infinito para asegurarse de que cualquier diferencia sea menor
    closest_date_difference = float('inf')

    #Se itera sobre todas las opciones encontradas 
    for option in options:

        #Esta linea de codigo obtiene el texto de la opcion actual.
        text = option.text

        #Lo que realiza find es extraer el texto que esta entre los parentesis
        # que se las posiciones del primer parentesis y del ultimo parentesis.
        # Obtener todas las opciones
        start_index = text.find('(') + 1
        end_index = text.find(')')

        #este almacena el texto entre esos dos indices
        date_str = text[start_index:end_index]

        # Separar la fecha en inicio y fin
        start_date_str, end_date_str = date_str.split(' / ')

        # Estas lineas convierten las cadenas de fecha en objetos datatime
        start_date = datetime.strptime(start_date_str, '%Y-%m-%d')
        end_date = datetime.strptime(end_date_str, '%Y-%m-%d')

        # Calcular la diferencia de días con la fecha actual
        start_difference = abs((start_date - present_date).days)
        end_difference = abs((end_date - present_date).days)

        # Elegir la opción con la fecha más cercana
        if start_difference < closest_date_difference:
            closest_date_option = option
            closest_date_difference = start_difference
        if end_difference < closest_date_difference:
            closest_date_option = option
            closest_date_difference = end_difference
        
    # Verificar si se encontró una opción válida antes de hacer clic
    if closest_date_option is not None:
        # Hacer clic en la opción con la fecha más cercana
        closest_date_option.click()
    else:
        print("No se encontró ninguna opción válida.")

    # Se espera dos segundos mas para poder descargar el documento
    time.sleep(2) 
    btn_download = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//input[@value="Descargar"]')))
    btn_download.click()

    time.sleep(15)
    driver.quit()


def connect_to_database():
    # Establecer conexión con la base de datos
    try:
        connection = mysql.connector.connect(
            host="127.0.0.1",
            port=3306,
            user="root",
            password="",
            database="proyecto"
        )
        return connection
    except mysql.connector.Error as error:
        print("Error al conectar a la base de datos: ", error)
        return None

def check_new_trimester():
    # Conectarse a la base de datos
    connection = connect_to_database()
    if connection:
        try:
            cursor = connection.cursor()

            # Obtener la fecha de inicio del trimestre más reciente
            query = "SELECT fecha_inicio FROM fechas_trimestre WHERE fecha_inicio <= NOW() AND fecha_fin >= NOW()"
            cursor.execute(query)

            last_trimester_start_date_result = cursor.fetchone()

            if last_trimester_start_date_result:
                last_trimester_start_date = last_trimester_start_date_result[0]
                current_date = datetime.now().date()

                # Verificar si ha comenzado un nuevo trimestre desde la última ejecución
                last_execution_file = "last_trimester.txt"
                try:
                    with open(last_execution_file, "r") as file:
                        last_execution_date = datetime.strptime(file.read().strip(), "%Y-%m-%d")
                except FileNotFoundError:
                    last_execution_date = datetime.min

                if current_date >= last_trimester_start_date and current_date != last_execution_date:
                    print("¡Ha comenzado un nuevo trimestre!")
                    run_code()
                    # Actualizar el archivo de última ejecución con la fecha actual
                    with open(last_execution_file, "w") as file:
                        file.write(current_date.strftime("%Y-%m-%d"))

                else:
                    print("Aún no ha comenzado un nuevo trimestre.")

            else:
                print("No se encontraron resultados para la consulta.")

            connection.close()
        except mysql.connector.Error as error:
            print("Error al ejecutar la consulta: ", error)

if __name__ == "__main__":
    # Ejecutar continuamente la verificación del nuevo trimestre
    while True:
        check_new_trimester()
        # Esperar un día antes de volver a verificar
        time.sleep(24 * 60 * 60)  # 24 horas en segundos