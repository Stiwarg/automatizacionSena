import os
import pandas as pd
from sqlalchemy import create_engine, DateTime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from datetime import datetime

# Ruta de la carpeta de descarga
#download_folder = "C:\\Users\\SENA\\Desktop\\bot\\bots\\documentos"
download_folder = "C:\\xampp\\htdocs\\bots\\documentos"


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
#mysql_engine = create_engine('mysql+mysqlconnector://root:@localhost/proyecto')

try:
    # Iniciar el navegador Chrome
    service = Service(executable_path=chrome_driver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)

    # Obtener la lista de archivos descargados con el mismo título
    archivos_descargados = os.listdir(download_folder)
    titulo_archivo = "Reporte_titulada_SAF"  # Ajusta esto según el título de tus archivos
    
    archivos_filtrados = [archivo for archivo in archivos_descargados if archivo.startswith(titulo_archivo)]
    
    # Ordenar la lista de archivos por fecha de modificación
    archivos_filtrados.sort(key=lambda x: os.path.getmtime(os.path.join(download_folder, x)))

    # Tomar el último archivo descargado con el mismo título
    ultimo_archivo = archivos_filtrados[-1]

    # Construir la ruta completa del último archivo descargado
    excel_file_path = os.path.join(download_folder, ultimo_archivo)

    # Leer el archivo Excel descargado
    df = pd.read_excel(excel_file_path, skiprows=4, header=None, names=['docu_instructor', 'instructores_id', 'programa_formacion', 'ficha', 'fecha_inicio_ficha', 'fecha_fin_ficha', 'fecha_inicio_programacion', 'fecha_fin_programacion', 'modalidad', 'jornada', 'grupo', 'dia_semana', 'ambiente', 'sede', 'hora_inicio', 'hora_fin', 'horas_programadas'])
    
    # Renombrar las columnas en el DataFrame
    df.rename(columns={'Documento Instructor': 'docu_instructor',
                       'Nombre Instructor': 'instructores_id',
                       'Programa de Formación': 'programa_formacion',
                       'Ficha': 'ficha',
                       'Fecha Inico de la Ficha': 'fecha_inicio_ficha',
                       'Fecha Fin de la Ficha': 'fecha_fin_ficha',
                       'Fecha Inicio Programación': 'fecha_inicio_programacion',
                       'Fecha Fin Programación': 'fecha_fin_programacion',
                       'Modalidad': 'modalidad',
                       'Jornada': 'jornada',
                       'Grupo': 'grupo',
                       'Dia Semana Programada': 'dia_semana',
                       'Ambiente Formación': 'ambiente',
                       'Sede': 'sede',
                       'Hora Inicio': 'hora_inicio',
                       'Hora Fin': 'hora_fin',
                       'Horas Programadas ': 'horas_programadas'}, inplace=True)
    
    # Convertir las fechas al tipo date
    date_columns = ['fecha_inicio_ficha', 'fecha_fin_ficha', 'fecha_inicio_programacion', 'fecha_fin_programacion']
    df[date_columns] = df[date_columns].apply(pd.to_datetime, format='%d-%m-%Y')
    df[date_columns] = df[date_columns].apply(lambda x: x.dt.date)

    # Obtener la fecha y hora actual para created_at
    now = datetime.now()

    # Añadir el campo created_at al DataFrame con la fecha y hora actual
    df['created_at'] = now

    df['instructor_id'] = None

    for index, row in df.iterrows():

        cedula_instructor = row['docu_instructor']

        querys_id = f"SELECT id FROM instructores WHERE identificacion = {cedula_instructor} "
        result = pd.read_sql_query(querys_id, con=mysql_engine)

        if not result.empty:
            df.at[index, 'instructor_id'] = result['id'].iloc[0]
        else:
            df.at[index, 'instructor_id'] = None
        
    df['instructor_id'] = df['instructor_id'].astype('Int64')

    df['instructores_id'] = df['instructor_id']

    df.drop(columns=['instructor_id'], inplace=True)
    # Consultar la base de datos para obtener los nombres que ya existen
    existing_nombres = pd.read_sql_query("SELECT grupo FROM carreras_tituladas", con=mysql_engine)

    # Filtrar el DataFrame para obtener solo los datos que no están en la base de datos
    df_to_insert = df[~df[['grupo']].apply(tuple, axis=1).isin(existing_nombres.apply(tuple, axis=1))]

    # Insertar los datos en la tabla existente en la base de datos MySQL
    if not df_to_insert.empty:
        df_to_insert.to_sql('carreras_tituladas', con=mysql_engine, if_exists='append', index=False, dtype={'created_at': DateTime})
        print("Datos insertados correctamente en la tabla carreras_tituladas.")
    else:
        print("No hay nuevos datos para insertar en la tabla carreras_tituladas.")

except Exception as e:
    print("Error:", e)

finally:
    # Cerrar el navegador y la conexión a la base de datos
    if 'driver' in locals():
        driver.quit()
    mysql_engine.dispose()
