#Se importa las bibliotecas necesarias de Selenium y Time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select 
from datetime import datetime, timedelta
from selenium.webdriver.common.keys import Keys

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

    input_document = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.ID, 'UsuarioDocumento')))
    input_document.send_keys("75077923")

    input_password = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.ID, 'UsuarioClave')))
    input_password.send_keys("Futuro2022")

    # Esperar a que aparezca el elemento div con la clase "submit"
    div_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//div[@class="submit"]'))
    )

    # Acceder al elemento input dentro del div
    btn_sign_in = div_element.find_element(By.XPATH, './/input[@class="btn btn-primary"]')
    btn_sign_in.click()



    combox_reportes = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, './/i[@class="fa fa-download"]')))
    combox_reportes.click()

    ul_reportes = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//ul[@class="treeview-menu menu-open"]')))
    asignacion_resultados = ul_reportes.find_element(By.XPATH, './/a[contains(text(), "reporte de novedades")]')

    asignacion_resultados.click()

    # Obtener la fecha actual
    fecha_actual = datetime.now()
    # Calcular la fecha tres semanas atrás
    fecha_inicial = fecha_actual - timedelta(weeks=1)
    # Formatear la fecha inicial como dia/mes/año
    fecha_inicial_str = fecha_inicial.strftime('%d/%m/%Y')

    # Obtener la fecha actual
    fecha_actual = datetime.now()
    # Formatear la fecha actual en el formato "día/mes/año" para darle la fecha final al bot
    fecha_final_str = fecha_actual.strftime('%d/%m/%Y')

    


    # Esperar a que aparezca el campo de fecha y hacer clic en él
    input_fecha = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'AsistenciaDiaInicial1')))
    input_fecha.click()

    # Limpiar el campo de fecha antes de enviar la fecha deseada
    input_fecha.clear()

    # Enviar la fecha deseada al campo de fecha
    input_fecha.send_keys(fecha_inicial_str)

    # Esperar a que aparezca el campo de fecha final y hacer clic en él
    input_fecha_final = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'AsistenciaDiaFinal1')))
    input_fecha_final.click()

    # Limpiar el campo de fecha final antes de enviar la fecha deseada
    input_fecha_final.clear()

    # Enviar la fecha deseada al campo de fecha final
    input_fecha_final.send_keys(fecha_final_str)

    time.sleep(2)  # Espera 2 segundos para asegurar que la página se haya cargado completamente
    btn_descargar = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Descargar")]')))
    btn_descargar.click()

    # Esperar antes de cerrar el navegador
    time.sleep(15)
    driver.quit()
def main():
    last_execution_file = "last_execution.txt"
    try:
        with open(last_execution_file, "r") as file:
            last_execution_date = datetime.strptime(file.read().strip(), "%Y-%m-%d")
    except FileNotFoundError:
        last_execution_date = datetime.min

    # Obtener la fecha actual
    current_date = datetime.now()

    # Calcular la fecha de la próxima ejecución (7 días después de la última ejecución)
    next_execution_date = last_execution_date + timedelta(days=7)

    # Ejecutar el código si ha pasado al menos una semana desde la última ejecución
    if current_date >= next_execution_date:
        run_code()

        # Actualizar el archivo de última ejecución con la fecha actual
        with open(last_execution_file, "w") as file:
            file.write(current_date.strftime("%Y-%m-%d"))

if __name__ == "__main__":
    main()