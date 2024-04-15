import os 
import pandas as pd
from sqlalchemy import create_engine, DateTime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from datetime import datetime

# Ruta de la carpeta de descarga
#download_folder = "C:\\Users\\SENA\\Desktop\\bot\\bots\\documentos"
download_folder = "C:\\xampp\\htdocs\\automatizacionSena\\bots\\documentos"


# Configurar las opciones de Chrome para la descarga
chrome_options = Options()
chrome_options.add_experimental_option("prefs", {
    "download.default_directory": download_folder,
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "safebrowsing.enabled": True
})


# Configurar la conexion a la base de datos MySQL en PhpMyAdmin
mysql_engine = create_engine('mysql+mysqlconnector://root:@localhost/prueba')

#mysql_engine = create_engine('mysql+mysqlconnector://root:@localhost/proyec')

try:

    archivos_descargados = os.listdir(download_folder)
    tile_file = "Instructores_Area"

    file_filters = [archivo for archivo in archivos_descargados if archivo.startswith(tile_file)]

    file_filters.sort(key=lambda x: os.path.getmtime(os.path.join(download_folder, x)))

    last_file = file_filters[-1]

    excel_file_path = os.path.join(download_folder, last_file)

    
    # Leer el archivo Excel sin encabezado
    df = pd.read_excel(excel_file_path)

    # Eliminar las primeras filas que contienen NaN
    df = df.dropna()
    print("aaaaaaa",df)
    df.rename(columns={'Documento': 'identificacion', 'Nombre Completos': 'nombre', 'Telefono': 'telefono', 'Correo': 'correo', 'AREA': 'area'}, inplace=True)

    df['tipo_contratos_id'] = 2
    now = datetime.now()

    df['created_at'] = now
    existing_nombres = pd.read_sql_query("SELECT identificacion FROM instructores_area", con=mysql_engine)
    df_to_insert = df[~df['identificacion'].isin(existing_nombres['identificacion'])]

    if not df_to_insert.empty:
        df_to_insert.to_sql('instructores_area', con=mysql_engine, if_exists='append', index=False, dtype={'created_at':DateTime})
        print("Datos insertados correctamente en la tabla instructores_area.")
    else:
        print("No hay nuevos datos para insertar en la tabla instructores_area.")

    print(df)

except Exception as e:
    print("Error:", e)

finally:
    # Cerrar el navegador y la conexión a la base de datos
    if 'driver' in locals():
     mysql_engine.dispose()