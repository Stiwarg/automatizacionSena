import os
import pandas as pd
from sqlalchemy import create_engine, DateTime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from datetime import datetime

# Ruta de la carpeta de descarga
download_folder = "C:\\xampp\htdocs\\automatizacionSena\\bots\\documentos"
#download_folder = "C:\\xampp\\htdocs\\bots\\documentos"

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
    titulo_archivo = "Reporte_Novedades"  # Ajusta esto según el título de tus archivos
    
    archivos_filtrados = [archivo for archivo in archivos_descargados if archivo.startswith(titulo_archivo)]
    
    # Ordenar la lista de archivos por fecha de modificación
    archivos_filtrados.sort(key=lambda x: os.path.getmtime(os.path.join(download_folder, x)))

    # Tomar el último archivo descargado con el mismo título
    ultimo_archivo = archivos_filtrados[-1]

    # Construir la ruta completa del último archivo descargado
    excel_file_path = os.path.join(download_folder, ultimo_archivo)

    # Leer el archivo Excel descargado
    df = pd.read_excel(excel_file_path, header=3)
    
    # Renombrar las columnas en el DataFrame
    columnas_renombradas = {'N°': 'novedad_numero', 'CURSO': 'curso', 'CÓDIGO FICHA': 'codigo_ficha', 'CÉDULA': 'cedula', 'NOMBRE APRENDIZ': 'nombre_aprendiz', 'TIPO NOVEDAD': 'tipo_novedad', 'SUBTIPO NOVEDAD': 'subtipo_novedad', 'NÚMERO RADICADO': 'numero_radicado', 'RADICADO RESPUESTA COORDIANCIÓN': 'radicado_respuesta', 'FECHA RESPUESTA': 'fecha_respuesta', 'OBSERVACIONES': 'observaciones', 'INSTRUCTORES NOTIFICADOS': 'noti_instructor', 'ESTADO NOVEDAD': 'estado_novedad', 'NUEVO CURSO': 'nuevo_curso', 'NOVEDAD REGISTRADA POR': 'novedad_registrada'}
    df.rename(columns=columnas_renombradas, inplace=True)
 
    df['id_aprendices'] = None 
    df['id_aprendices'] = df['id_aprendices'].astype('Int64')

    for index, row in df.iterrows():
        
        identificacion_aprendiz = row['cedula']
        querys_id = f"SELECT id FROM aprendices WHERE identificacion_aprendiz = {identificacion_aprendiz} "
        result = pd.read_sql_query(querys_id, con=mysql_engine)

        if not result.empty:
            df.at[index,'id_aprendices'] = result['id'].iloc[0]
        else:
            df.at[index,'id_aprendices'] = None
    
    # Obtener la fecha y hora actual para created_at
    now = datetime.now() 

    # Añadir el campo created_at al DataFrame con la fecha y hora actual
    df['created_at'] = now

    # Consultar la base de datos para obtener los números de radicado que ya existen
    existing_numeros_radicado = pd.read_sql_query("SELECT numero_radicado FROM novedades_respondidas", con=mysql_engine)

    # Filtrar el DataFrame para obtener solo los datos que no están en la base de datos
    df_to_insert = df[~df['numero_radicado'].isin(existing_numeros_radicado['numero_radicado'])]

    # Insertar los datos en la tabla existente en la base de datos MySQL
    if not df_to_insert.empty:
        columns_to_insert = ['novedad_numero', 'curso', 'codigo_ficha', 'cedula', 'nombre_aprendiz', 'tipo_novedad', 'subtipo_novedad', 'numero_radicado', 'radicado_respuesta', 'fecha_respuesta', 'observaciones', 'noti_instructor', 'estado_novedad', 'nuevo_curso', 'novedad_registrada', 'id_aprendices', 'created_at']
        df_to_insert_selected = df_to_insert[columns_to_insert]
        df_to_insert_selected.to_sql('novedades_respondidas', con=mysql_engine, if_exists='append', index=False, dtype={'created_at': DateTime})
        print("Datos insertados correctamente en la tabla novedades_respondidas.")
    else:
        print("No hay nuevos datos para insertar en la tabla novedades_respondidas.")

except Exception as e:
    print("Error:", e)

finally:
    # Cerrar el navegador y la conexión a la base de datos
    if 'driver' in locals():
     mysql_engine.dispose()
