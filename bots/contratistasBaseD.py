import os
import pandas as pd
from sqlalchemy import create_engine, DateTime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from datetime import datetime

# Ruta de la carpeta de descarga
download_folder = "C:\\Users\\SENA\\Desktop\\bot\\bots\\documentos"
#download_folder = "C:\\xampp\\htdocs\\bots\\documentos"


# Configurar las opciones de Chrome para la descarga
chrome_options = Options()
chrome_options.add_experimental_option("prefs", {
    "download.default_directory": download_folder,
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "safebrowsing.enabled": True
})

# Ruta del controlador de Chrome
chrome_driver_path = r"C:\dchrome\chromedriver.exe"

# Configurar la conexión a la base de datos MySQL en PhpMyAdmin
mysql_engine = create_engine('mysql+mysqlconnector://root:@localhost/proyect')

try:
    # Iniciar el navegador Chrome
    service = Service(executable_path=chrome_driver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)
    
    # ... Código para navegar y descargar el archivo Excel omitido por claridad ...

    # Obtener la lista de archivos descargados con el mismo título
    archivos_descargados = os.listdir(download_folder)
    titulo_archivo = "Datos_Contratistas_"  # Ajusta esto según el título de tus archivos
    
    archivos_filtrados = [archivo for archivo in archivos_descargados if archivo.startswith(titulo_archivo)]
    
    # Ordenar la lista de archivos por fecha de modificación
    archivos_filtrados.sort(key=lambda x: os.path.getmtime(os.path.join(download_folder, x)))

    # Tomar el último archivo descargado con el mismo título
    ultimo_archivo = archivos_filtrados[-1]

    # Construir la ruta completa del último archivo descargado
    excel_file_path = os.path.join(download_folder, ultimo_archivo)

    # Leer el archivo Excel descargado
    df = pd.read_excel(excel_file_path)
    
    # Renombrar la columna en el DataFrame
    df.rename(columns={'Nombre del contratista': 'nombre'}, inplace=True)
    df.rename(columns={'Identificación': 'identificacion'}, inplace=True)
    df.rename(columns={'Programa': 'programa'}, inplace=True)
    df.rename(columns={'Supervisor': 'supervisor'}, inplace=True)
    df.rename(columns={'CORREO': 'correo'}, inplace=True)
    df.rename(columns={'TELEFONO': 'telefono'}, inplace=True)
    df['tipo_contratos_id'] = 1
    df['instructores_area_id'] = 1

    # Obtener la fecha y hora actual para created_at
    now = datetime.now()

    # Añadir el campo created_at al DataFrame con la fecha y hora actual
    df['created_at'] = now

    # Consultar la base de datos para obtener los nombres que ya existen
    existing_nombres = pd.read_sql_query("SELECT nombre FROM instructores", con=mysql_engine)

    # Filtrar el DataFrame para obtener solo los datos que no están en la base de datos
    df_to_insert = df[~df['nombre'].isin(existing_nombres['nombre'])]

    # Insertar los datos en la tabla existente en la base de datos MySQL
    if not df_to_insert.empty:
        df_to_insert.to_sql('instructores', con=mysql_engine, if_exists='append', index=False, dtype={'created_at': DateTime})
        print("Datos insertados correctamente en la tabla instructores.")
    else:
        print("No hay nuevos datos para insertar en la tabla instructores.")

except Exception as e:
    print("Error:", e)

finally:
    # Cerrar el navegador y la conexión a la base de datos
    if 'driver' in locals():
        driver.quit()
    mysql_engine.dispose()
