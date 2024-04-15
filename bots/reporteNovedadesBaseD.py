import os
import pandas as pd
from sqlalchemy import create_engine, DateTime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from datetime import datetime

# Ruta de la carpeta de descarga
download_folder = "C:\\xampp\\htdocs\\automatizacionSena\\bots\\documentos"

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
    # ... Código para navegar y descargar el archivo Excel omitido por claridad ...

    # Obtener la lista de archivos descargados con el mismo título
    archivos_descargados = os.listdir(download_folder)
    titulo_archivo = "Reporte Novedades en Tramite SAF"  # Ajusta esto según el título de tus archivos
    
    archivos_filtrados = [archivo for archivo in archivos_descargados if archivo.startswith(titulo_archivo)]
    
    # Ordenar la lista de archivos por fecha de modificación
    archivos_filtrados.sort(key=lambda x: os.path.getmtime(os.path.join(download_folder, x)))

    # Tomar el último archivo descargado con el mismo título
    ultimo_archivo = archivos_filtrados[-1]

    # Construir la ruta completa del último archivo descargado
    excel_file_path = os.path.join(download_folder, ultimo_archivo)

    # Leer el archivo Excel descargado
    df = pd.read_excel(excel_file_path, skiprows=3, parse_dates=[4], names=['ficha', 'grupo', 'documento', 'nombre', 'fecha_registro', 'reportado'])
    # Renombrar las columnas en el DataFrame
    df.rename(columns={'Ficha': 'ficha',
                       'Grupo': 'grupo',
                       'Nombre':'nombre',
                       'Documento': 'documento',
                       'Fecha registro': 'fecha_registro',
                       'Reportado por': 'reportado'}, inplace=True)


    # Convertir la columna 'Fecha registro' a tipo de fecha
    df['fecha_registro'] = pd.to_datetime(df['fecha_registro'], format='%Y-%m-%d')

    # Añadir el campo 'aprendices_id' al DataFrame
    df['aprendices_id'] = 1

    # Obtener la fecha y hora actual para created_at
    now = datetime.now()

    # Añadir el campo created_at al DataFrame con la fecha y hora actual
    df['created_at'] = now

    # Consultar la base de datos para obtener los nombres que ya existen
    existing_nombres = pd.read_sql_query("SELECT fecha_registro FROM aprendices_novedades", con=mysql_engine)
    existing_nombres['fecha_registro'] = pd.to_datetime(existing_nombres['fecha_registro'])
    df_to_insert = df[~df['fecha_registro'].isin(existing_nombres['fecha_registro'])]


    # Insertar los datos en la tabla existente en la base de datos MySQL
    if not df_to_insert.empty:
        df_to_insert.to_sql('aprendices_novedades', con=mysql_engine, if_exists='append', index=False, dtype={'created_at': DateTime})
        print("Datos insertados correctamente en la tabla aprendices_novedades.")
    else:
        print("No hay nuevos datos para insertar en la tabla aprendices_novedades.")

except Exception as e:
    print("Error:", e)

finally:
    # Cerrar el navegador y la conexión a la base de datos
    if 'driver' in locals():
      mysql_engine.dispose()
