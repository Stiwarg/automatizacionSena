import os
import pandas as pd
from sqlalchemy import create_engine, DateTime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from datetime import datetime
import time  # Importar la biblioteca time


# Ruta de la carpeta de descarga
#download_folder = "C:\\Users\\SENA\\Desktop\\bot\\bots\\documentos"
download_folder = "C:\\xampp\htdocs\\automatizacionSena\\bots\\documentos"


# Configurar las opciones de Chrome para la descarga
chrome_options = Options()
chrome_options.add_experimental_option("prefs", {
    "download.default_directory": download_folder,
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "safebrowsing.enabled": True
})
# Configurar la conexión a la base de datos MySQL en PhpMyAdmin
mysql_engine = create_engine('mysql+mysqlconnector://root:@localhost/prueba')

try:
    # Obtener la lista de archivos descargados con el mismo título
    archivos_descargados = os.listdir(download_folder)
    titulo_archivo = "PLANTA_2024_BD"  # Ajusta esto según el título de tus archivos
    
    archivos_filtrados = [archivo for archivo in archivos_descargados if archivo.startswith(titulo_archivo)]
    
    # Ordenar la lista de archivos por fecha de modificación
    archivos_filtrados.sort(key=lambda x: os.path.getmtime(os.path.join(download_folder, x)))

    # Tomar el último archivo descargado con el mismo título
    ultimo_archivo = archivos_filtrados[-1]

    # Construir la ruta completa del último archivo descargado
    excel_file_path = os.path.join(download_folder, ultimo_archivo)

    # Leer el archivo Excel descargado
    df = pd.read_excel(excel_file_path)
    
    df = df.dropna()

    # Renombrar las columnas necesarias
    df.rename(columns={'Documento': 'identificacion', 'Nombre': 'nombre', 'Apellido': 'apellidos', 
                               'Telefono': 'telefono', 'Correo': 'correo', 'AREA': 'instructores_area_id'}, inplace=True)
    
    # Asignar valores a las columnas adicionales
    df['tipo_contratos_id'] = 2

    # Obtener la fecha y hora actual para created_at
    now = datetime.now()

    df['instructor_area'] = None

    for index, row in df.iterrows():

        area_instructor = row['instructores_area_id']
        querys_id_area = f"SELECT id FROM instructores_area WHERE area = '{area_instructor}' "
        result = pd.read_sql_query(querys_id_area, con=mysql_engine)
        print("Resultados de la consulta: ", result)
        if not result.empty:
            df.at[index, 'instructor_area'] = result['id'].iloc[0]
        else: 
            df.at[index, 'instructor_area'] = None

    time.sleep(0.1)    
    
    df['instructor_area'] = df['instructor_area'].astype('Int64')
    df['instructores_area_id'] = df['instructor_area']

    df.drop(columns=['instructor_area'], inplace=True)
    

    # Añadir el campo created_at al DataFrame con la fecha y hora actual
    df['created_at'] = now
    df['updated_at'] = now
    # Consultar la base de datos para obtener los nombres que ya existen
    existing_nombres = pd.read_sql_query("SELECT nombre FROM instructores", con=mysql_engine)

    # Filtrar el DataFrame para obtener solo los datos que no están en la base de datos
    df_to_insert = df[~df['nombre'].isin(existing_nombres['nombre'])]

    # Insertar los datos en la tabla existente en la base de datos MySQL
    if not df_to_insert.empty:
        df_to_insert.to_sql('instructores', con=mysql_engine, if_exists='append', index=False, dtype={'created_at': DateTime,'updated_at': DateTime})
        print("Datos insertados correctamente en la tabla instructores.")
    else:
        print("No hay nuevos datos para insertar en la tabla instructores.")

except Exception as e:
    print("Error:", e)

finally:
    # Cerrar el navegador y la conexión a la base de datos
    if 'driver' in locals():
     mysql_engine.dispose()