#Se importan las bibliotecas necesarias de Selenium y otras utilidades:
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select 

#Se define la carpeta de descarga para los archivos descargados:
download_folder = "C:\\Users\\SENA\\Desktop\\bot\\documentos"


# Configurar las opciones de Chrome para la descarga
chrome_options = Options()
chrome_options.add_experimental_option("prefs", {
  "download.default_directory": download_folder,
  "download.prompt_for_download": False,
  "download.directory_upgrade": True,
  "safebrowsing.enabled": True
})

#Se crea un servicio de Chrome Webdriver y se inicia el navegador Chrome con las opciones configuradas anteriormente:
service = Service(executable_path=r"C:\dchrome\chromedriver.exe")
driver = webdriver.Chrome(service=service, options=chrome_options)

#Se navega a la página web
driver.get("http://senasofiaplus.edu.co/sofia-public/")

#Se espera a que aparezca el elemento iframe con el ID 'registradoBox1' y se cambia al marco (frame) de ese iframe:
iframe = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.ID, 'registradoBox1')))
driver.switch_to.frame(iframe)

#se crea un objeto que permite al script esperar hasta que se cumpla una determinada condicion en el navegador web
wait = WebDriverWait(driver, 20)

#Se encuentra el campo de entrada de documento (username), se ingresa la información y se hace clic en el botón de inicio de sesión:
input_document = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input.input100[name='ingreso'][id='username']")))
input_document.send_keys("1109662945")

input_document2 = wait.until(EC.presence_of_element_located((By.NAME, "josso_password")))
input_document2.send_keys("1109662945Gonzalez")

btn_document = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "login100-form-btn")))
btn_document.click()

#Se cambia al contenido predeterminado (default content) del navegador:
driver.switch_to.default_content()

#Se selecciona un valor en un menú desplegable por su ID y se hace clic en un enlace de la página:
select_document = wait.until(EC.presence_of_element_located((By.ID, "seleccionRol:roles")))
select = Select(select_document)
select.select_by_value('5')
time.sleep(2)
registro_link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[contains(span/text(),'Registro')]")))
registro_link.click()

#Se encuentran y hacen clic en los enlaces de la página para navegar más profundamente:
registro_persona_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//ul[@class='nav nav-second-level collapse in']/li/a[contains(text(), 'Registro Persona')]"))
    )
registro_persona_link.click()
li_document = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//ul[@class='nav nav-third-level collapse in']/li/a[contains(text(), 'Documentos')]")))
li_document.click()

#Se espera a que aparezca un iframe específico, se cambia a ese iframe y se hace clic en un icono dentro de ese iframe:
iframe2 = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.ID, 'contenido')))
driver.switch_to.frame(iframe2)
icono_elemento = WebDriverWait(driver, 30).until(
    EC.element_to_be_clickable((By.XPATH, "//a[@id='Listado:tablaDocumentosCargados:0:cmdlnkDescargarArc']/img[@id='Listado:tablaDocumentosCargados:0:imgDetallejj']"))
)
# Hacer clic en el elemento utilizando JavaScript
driver.execute_script("arguments[0].click();", icono_elemento)

#Se vuelve al contenido predeterminado del navegador
driver.switch_to.default_content()

#Se espera por un período de 30 segundos antes de cerrar el navegador:
time.sleep(30)
driver.quit()
