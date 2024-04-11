
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select 


service = Service(executable_path=r"C:\dchrome\chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("http://senasofiaplus.edu.co/sofia-public/")

iframe = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.ID, 'registradoBox1')))

driver.switch_to.frame(iframe)

wait = WebDriverWait(driver, 20)

input_document = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input.input100[name='ingreso'][id='username']")))

input_document.send_keys("1109662945")

input_document2 = wait.until(EC.presence_of_element_located((By.NAME, "josso_password")))
input_document2.send_keys("1109662945Gonzalez")

btn_document = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "login100-form-btn")))

btn_document.click()

driver.switch_to.default_content()

select_document = wait.until(EC.presence_of_element_located((By.ID, "seleccionRol:roles")))

select = Select(select_document)

select.select_by_value('5')

time.sleep(2)

registro_link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[contains(span/text(),'Registro')]")))

registro_link.click()

registro_persona_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//ul[@class='nav nav-second-level collapse in']/li/a[contains(text(), 'Registro Persona')]"))
    )

registro_persona_link.click()

li_document = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//ul[@class='nav nav-third-level collapse in']/li/a[contains(text(), 'Documentos')]")))

li_document.click()

iframe2 = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.ID, 'contenido')))
driver.switch_to.frame(iframe2)


icono_elemento = WebDriverWait(driver, 60).until(
    EC.element_to_be_clickable((By.XPATH, "//a[@id='Listado:tablaDocumentosCargados:0:cmdlnkDescargarArc']/img[@id='Listado:tablaDocumentosCargados:0:imgDetallejj']"))
)

# Hacer clic en el elemento utilizando JavaScript
driver.execute_script("arguments[0].click();", icono_elemento)
#tienen que descargar en icon_document

#icono_elemento.click()

driver.switch_to.default_content()
print("fff")

time.sleep(80)
driver.quit()
