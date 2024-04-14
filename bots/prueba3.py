from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

def open_browser():
    # Configurar las opciones de Chrome
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")  # Maximizar la ventana al abrir el navegador

    # Iniciar el servicio de Chrome WebDriver y el navegador Chrome con las opciones configuradas
    service = Service(executable_path=r"C:\chromedriver.exe")
    driver = webdriver.Chrome(service=service, options=chrome_options)

    # Abrir una página web (en este caso, simplemente sobre:blank)
    driver.get("about:blank")

if __name__ == "__main__":
    open_browser()
