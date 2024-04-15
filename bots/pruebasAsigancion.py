import os
import pandas as pd
from sqlalchemy import create_engine, DateTime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from datetime import datetime

# Ruta de la carpeta de descarga
download_folder = "C:\\xampp\\htdocs\\automatizacionSena\\bots\\documentos"
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
mysql_engine = create_engine('mysql+mysqlconnector://root:@localhost/proyect')

try:

    # ... Código para navegar y descargar el archivo Excel omitido por claridad ...

    # Obtener la lista de archivos descargados con el mismo título
    archivos_descargados = os.listdir(download_folder)
    titulo_archivo = "Reporte_asignacion"  # Ajusta esto según el título de tus archivos
    
    archivos_filtrados = [archivo for archivo in archivos_descargados if archivo.startswith(titulo_archivo)]
    
    # Ordenar la lista de archivos por fecha de modificación
    archivos_filtrados.sort(key=lambda x: os.path.getmtime(os.path.join(download_folder, x)))

    # Tomar el último archivo descargado con el mismo título
    ultimo_archivo = archivos_filtrados[-1]

    # Construir la ruta completa del último archivo descargado
    excel_file_path = os.path.join(download_folder, ultimo_archivo)

    # Leer el archivo Excel descargado
    df = pd.read_excel(excel_file_path, header=3)  # El índice 3 corresponde a la cuarta fila
    # Renombrar las columnas en el DataFrame
    df.rename(columns={'CÉDULA': 'cedula', 'INSTRUCTOR RESPONSABLE': 'instructor_responsable',
                       'CODIGO PROGRAMA': 'codigo_programa', 'PROGRAMA DE FORMACIÓN': 'programa_formacion',
                       'NÚMERO FICHA': 'numero_ficha', 'CURSO': 'curso', 'TRIMESTRE DEL CURSO': 'trimestre_curso',
                       'TRIMESTRE DEL AÑO': 'trimestres_id', 'COMPETENCIA': 'competencia', 'RESULTADO': 'resultado',
                       'ACTIVIDAD PROYECTO': 'actividad_proyecto', 'RESPONSABLE EVALUAR RESULTADO': 'responsable_evaluacion'}, inplace=True)
    
    # Inicializar la columna 'instructor_id' con valores nulos  
    df['instructor_id'] = None

    # Iterar sobre cada fila del DataFrame
    for index, row in df.iterrows():
        # Obtener la cédula del instructor de la fila actual
        cedula_instructor = row['cedula']
        # Consultar la base de datos para obtener el ID del instructor usando la cédula
        querys_id = f"SELECT id FROM instructores WHERE identificacion = {cedula_instructor} "
        result = pd.read_sql_query(querys_id, con=mysql_engine)

        # Verificar si la consulta retornó algún resultado
        if not result.empty:
            # Asignar el ID del instructor a la columna 'instructor_id' de la fila actual
            df.at[index, 'instructor_id'] = result['id'].iloc[0]
        else: 
            # Si no se encontró el ID del instructor, asignar None a la columna 'instructor_id'
            df.at[index, 'instructor_id'] = None
    
    # Convertir la columna 'instructor_id' a tipo de dato int
    df['instructor_id'] = df['instructor_id'].astype('Int64')

    # Reemplazar 'instructor_responsable' con 'instructor_id'
    df['instructor_responsable'] = df['instructor_id']
    # Eliminar la columna temporal 'instructor_id'
    df.drop(columns=['instructor_id'], inplace=True)

    # Obtener la fecha y hora actual para created_at
    now = datetime.now()

    # Añadir el campo created_at al DataFrame con la fecha y hora actual
    df['created_at'] = now

    # Consultar la base de datos para obtener los nombres que ya existen
    existing_nombres = pd.read_sql_query("SELECT trimestres_id FROM resultados_asignados", con=mysql_engine)

    # Filtrar el DataFrame para obtener solo los datos que no están en la base de datos
    df_to_insert = df[~df['trimestres_id'].isin(existing_nombres['trimestres_id'])]

    if not df_to_insert.empty:
        df_to_insert.to_sql('resultados_asignados', con=mysql_engine, if_exists='append', index=False, dtype={'created_at': DateTime})
        print("Datos insertados correctamente en la tabla resultados_asignados.")
    else:
        print("No hay nuevos datos para insertar en la tabla resultados_asignados.")

except Exception as e:
    print("Error:", e)

finally:
    # Cerrar el navegador y la conexión a la base de datos
    if 'driver' in locals():
        mysql_engine.dispose()
