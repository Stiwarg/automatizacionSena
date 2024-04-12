import os
import pandas as pd
from sqlalchemy import create_engine, DateTime
from sqlalchemy.sql import func
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from datetime import datetime
from sqlalchemy.sql import text
# Ruta de la carpeta de descarga
download_folder = "C:\\Users\\SENA\\Desktop\\bot\\bots\\documentos"

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
    titulo_archivo = "ReportedeJuiciosEvaluativos"  # Ajusta esto según el título de tus archivos
    
    archivos_filtrados = [archivo for archivo in archivos_descargados if archivo.startswith(titulo_archivo)]
    
    # Ordenar la lista de archivos por fecha de modificación
    archivos_filtrados.sort(key=lambda x: os.path.getmtime(os.path.join(download_folder, x)))

    # Tomar el último archivo descargado con el mismo título
    ultimo_archivo = archivos_filtrados[-1]

    # Construir la ruta completa del último archivo descargado
    excel_file_path = os.path.join(download_folder, ultimo_archivo)

    # Leer el archivo Excel descargado
    df = pd.read_excel(excel_file_path, skiprows=lambda x: x in range(1, 13), names=['tipo_documento', 'identificacion_aprendiz', 'nombre_aprendiz', 
                                                                       'apellidos_aprendiz', 'estado_formacion', 'competencias', 'resultado',
                                                                       'juicio_evaluativo', 'funcionario_registro'])
    # Leer el archivo Excel descargado para obtener solo las fechas
    df_fechas = pd.read_excel(excel_file_path, usecols=[2], names=['Fechas'], header=None)

    # Filtrar las filas necesarias
    df_fechas = df_fechas.iloc[[1, 7, 8]]

    # Obtener las fechas en las filas específicas
    FechaReporte = pd.to_datetime(df_fechas.iloc[0, 0], errors='coerce')  # Fila 2, Columna 0 (primera columna)
    FechaInicio = pd.to_datetime(df_fechas.iloc[1, 0], errors='coerce')  # Fila 8, Columna 0 (primera columna)
    FechaFin = pd.to_datetime(df_fechas.iloc[2, 0], errors='coerce')  # Fila 9, Columna 0 (primera columna)
    
    existing_nombres = pd.read_sql_query("SELECT nombre_aprendiz FROM aprendices", con=mysql_engine)

    # Filtrar el DataFrame para obtener solo los datos que no están en la base de datos
    df_to_insert = df[~df['nombre_aprendiz'].isin(existing_nombres['nombre_aprendiz'])]

    # Convertir las fechas a formato de fecha de MySQL (YYYY-MM-DD)
    FechaReporte = FechaReporte.strftime('%Y-%m-%d %H:%M:%S')
    FechaInicio = FechaInicio.strftime('%Y-%m-%d %H:%M:%S')
    FechaFin = FechaFin.strftime('%Y-%m-%d %H:%M:%S')

    
    # Obtener el primer ID de la tabla instructores
    primer_id = None
    with mysql_engine.connect() as connection:
        query = text("SELECT id FROM instructores ORDER BY id LIMIT 1")
        result = connection.execute(query)
        row = result.fetchone()
    if row:
        primer_id = row[0]

    # Utilizar el primer ID obtenido como sea necesario
    if primer_id is not None:
        print("El primer ID en la tabla instructores es:", primer_id)
    else:
        print("No se encontraron registros en la tabla instructores.")

    # Obtener la fecha y hora actual
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # Insertar los datos en la tabla existente en la base de datos MySQL
    if not df_to_insert.empty:
        # Crear una lista de diccionarios para insertar en la tabla
        data_to_insert = []
        for index, row in df_to_insert.iterrows():
            data = {
                'fecha_reporte': FechaReporte,
                'fecha_inicio': FechaInicio,
                'fecha_fin': FechaFin,
                'tipo_documento': row['tipo_documento'],
                'identificacion_aprendiz': row['identificacion_aprendiz'],
                'nombre_aprendiz': row['nombre_aprendiz'],
                'apellidos_aprendiz': row['apellidos_aprendiz'],
                'estado_formacion': row['estado_formacion'],
                'competencias': row['competencias'],
                'resultado': row['resultado'],
                'juicio_evaluativo': row['juicio_evaluativo'],
                'funcionario_registro': row['funcionario_registro'],
                'created_at': now,
                'updated_at': now,  # Se establece con la fecha y hora actual
                'instructores_id': primer_id  # Usar el primer ID de la tabla instructores
            }
            data_to_insert.append(data)

        # Insertar los datos en la tabla existente en la base de datos MySQL
        pd.DataFrame(data_to_insert).to_sql('aprendices', con=mysql_engine, if_exists='append', index=False,
                                            dtype={'created_at': DateTime, 'updated_at': DateTime},
                                            index_label='id')
        print("Datos insertados correctamente en la tabla aprendices.")
    else:
        print("No hay nuevos datos para insertar en la tabla aprendices.")
except Exception as e:
    print("Error:", e)

finally:
    # Cerrar el navegador y la conexión a la base de datos
    if 'driver' in locals():
        mysql_engine.dispose()
