
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



download_folder = "C:\\Users\\SENA\\Desktop\\bot\\bots\\documentos"

chrome_options = Options()
chrome_options.add_experimental_option("prefs",{
        "download.default_directory":download_folder,
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing.enabled": True
    })

service = Service(executable_path=r"C:\dchrome\chromedriver.exe")
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get("https://onedrive.live.com/login/")

iframe = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.CLASS_NAME, 'signInFrame')))
driver.switch_to.frame(iframe)

input_email = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.CLASS_NAME, 'form-control')))

input_email.send_keys("jegonzalez549@soy.sena.edu.co")

btn_next = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, "//input[@class='btn btn-block btn-primary' and @value='Siguiente']")))
btn_next.click()
driver.switch_to.default_content()

input_password = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.NAME, "passwd")))

input_password.send_keys("123456789Gonzalez")

btn_session = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.ID, "idSIButton9")))
btn_session.click()

div_mantener_session = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.ID, "lightboxTemplateContainer")))
btn_mantener = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, "//input[@value='Sí']")))
btn_mantener.click()

navigation_panel = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'navIconContainer_239d9f93')]/button[contains(@class, 'navIconButton_239d9f93')]/div[contains(@class, 'navIcon_239d9f93')]/i[contains(@class, 'icon_52314de0')][@name='OpenPaneMirrored']")))
navigation_panel.click()

element_compart = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, "//ul[@class='groupItems_94cbd27d']//li[contains(@class, 'navLink_7c3aa882')]//a[@title='Compartido']")))
element_compart.click()

navigation_panel_2 = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'navIconContainer_239d9f93')]/button[contains(@class, 'navIconButton_239d9f93')]/div[contains(@class, 'navIcon_239d9f93')]/i[contains(@class, 'icon_52314de0')][@name='ClosePaneMirrored']")))
navigation_panel_2.click()

element_folder = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, "//button[contains(@title, 'Juicios Evaluativos')]")))
element_folder.click()

element_changed = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.ID, "header29-dateModifiedColumn_902-name")))
element_changed.click()

time.sleep(80)
driver.quit()