import os
import pandas as pd
from sqlalchemy import create_engine, DateTime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from datetime import datetime
import time


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

# Ruta del controlador de Chrome


# Configurar la conexión a la base de datos MySQL en PhpMyAdmin
#mysql_engine = create_engine('mysql+mysqlconnector://root:@localhost/proyectoo')
mysql_engine = create_engine('mysql+mysqlconnector://root:@localhost/prueba')
#mysql_engine = create_engine('mysql+mysqlconnector://root:@localhost/proyecto')

try:
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
    df = pd.read_excel(excel_file_path, skiprows=4, header=None, names=['docu_instructor', 'instructores_id', 'programa_formacion', 'cursos_id', 'fecha_inicio_ficha', 'fecha_fin_ficha', 'fecha_inicio_programacion', 'fecha_fin_programacion', 'modalidad', 'jornada', 'grupo', 'dia_semana', 'ambiente', 'sede', 'hora_inicio', 'hora_fin', 'horas_programadas'])
    
    # Renombrar las columnas en el DataFrame
    df.rename(columns={'Documento Instructor': 'docu_instructor',
                       'Nombre Instructor': 'instructores_id',
                       'Programa de Formación': 'programa_formacion',
                       'Ficha': 'cursos_id',
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

    #Se crea una nueva columna llamada 'instructor_id' en el DataFrame df y se inicializa con valores None
    df['instructor_id'] = None
    # Se itera sobre cada fila del DataFrame df. index es el índice de la fila y row es una serie que contiene los datos de la fila actual.
    for index, row in df.iterrows():
        # Se obtiene el valor de la columna 'docu_instructor' de la fila actual y se almacena en la variable 
        cedula_instructor = row['docu_instructor']
        #Se construye una consulta SQL para seleccionar el ID del instructor correspondiente a la identificación (identificacion) obtenida en el paso anterior.
        querys_id = f"SELECT id FROM instructores WHERE identificacion = {cedula_instructor} "
        result = pd.read_sql_query(querys_id, con=mysql_engine)
        # Se verifica si el DataFrame result no está vacío, lo que significa que se encontró un instructor con la identificación proporcionada.
        if not result.empty:
            #Si se encontró un instructor, se asigna su ID a la columna 'instructor_id' en la fila correspondiente del DataFrame df.
            df.at[index, 'instructor_id'] = result['id'].iloc[0]
        else:
            #En caso contrario, si no se encontró ningún instructor, se asigna None a la columna 'instructor_id' en la fila correspondiente del DataFrame df.
            df.at[index, 'instructor_id'] = None
    # Se convierten los valores en la columna 'instructor_id' a tipo de datos entero     
    df['instructor_id'] = df['instructor_id'].astype('Int64')
    #Se crea una nueva columna llamada 'instructores_id' en el DataFrame df y se copian los valores de la columna 'instructor_id'.
    df['instructores_id'] = df['instructor_id']
    #Se elimina la columna 'instructor_id' del DataFrame df.
    df.drop(columns=['instructor_id'], inplace=True)

    # Guardar los datos en la tabla "cursos" sin duplicados
    df_cursos = df[['cursos_id', 'grupo', 'programa_formacion']].drop_duplicates()
    df_cursos.rename(columns={'cursos_id': 'ficha'}, inplace=True)
    

    # Verificar si hay datos en df_cursos
    if not df_cursos.empty:
        # Construir una consulta SQL para seleccionar los grupos existentes en la tabla "cursos"
        query_existing_groups = "SELECT DISTINCT grupo FROM cursos"
        
        # Ejecutar la consulta SQL en la base de datos
        existing_groups = pd.read_sql_query(query_existing_groups, con=mysql_engine)
        
        # Filtrar df_cursos para excluir los grupos que ya existen en la tabla "cursos"
        df_cursos_to_insert = df_cursos[~df_cursos['grupo'].isin(existing_groups['grupo'])].dropna()
        
        # Verificar si hay filas para insertar
        if not df_cursos_to_insert.empty:
            # Insertar las filas que no están en la tabla "cursos"
            df_cursos_to_insert.to_sql('cursos', con=mysql_engine, if_exists='append', index=False)
            print("Datos insertados correctamente en la tabla cursos.")
        else:
            print("No hay nuevos datos para insertar en la tabla cursos.")
    else:
        print("El DataFrame df_cursos está vacío.")

    time.sleep(0.1)

    # Renombrar la columna 'ficha' a 'cursos_id' en el DataFrame df
    df.rename(columns={'ficha': 'cursos_id'}, inplace=True)
    df['curso_id'] = None

    for index, row in df.iterrows():
        # Construir una consulta SQL para seleccionar el ID del curso correspondiente utilizando los valores de 'cursos_id', 'grupo' y 'programa_formacion' de la fila actual
        query_id_curso = f"SELECT id FROM cursos WHERE ficha = {row['cursos_id']} "
        
        # Ejecutar la consulta SQL en la base de datos
        result = pd.read_sql_query(query_id_curso, con=mysql_engine)

        # Verificar si se encontró un curso
        if not result.empty:
            # Asignar el ID del curso a la columna 'curso_id' en el DataFrame df
            df.at[index, 'curso_id'] = result['id'].iloc[0]
        else:
            # Si no se encontró ningún curso, asignar None a la columna 'curso_id'
            df.at[index, 'curso_id'] = None
    
    time.sleep(0.2)  
    # Convertir los valores en la columna 'curso_id' a tipo de datos entero
    df['curso_id'] = df['curso_id'].astype('Int64')  
    # Crear una nueva columna llamada 'cursos_id' en el DataFrame df y copiar los valores de la columna 'curso_id'
    df['cursos_id'] = df['curso_id']
    # Eliminar la columna 'curso_id' del DataFrame df
    df.drop(columns=['curso_id'], inplace=True)

    # Consultar la base de datos para obtener los nombres de grupo que ya existen en la tabla "cursos"
    existing_nombres = pd.read_sql_query("SELECT DISTINCT grupo FROM cursos", con=mysql_engine)
    # Consultar la base de datos para obtener los nombres que ya existen
    existing_nombres = pd.read_sql_query("SELECT grupo FROM carreras_tituladas", con=mysql_engine)
    # Filtrar el DataFrame para obtener solo los datos que no están en la base de datos
    df_to_insert = df[~df['grupo'].isin(existing_nombres['grupo'])]

    # Insertar los datos en la tabla existente en la base de datos MySQL
    if not df_to_insert.empty:
        df_to_insert.to_sql('carreras_tituladas', con=mysql_engine, if_exists='append', index=False, dtype={'created_at': DateTime})
        print("Datos insertados correctamente en la tabla carreras_tituladas")
    else:
        print("No hay nuevos datos para insertar en la tabla carreras_tituladas.")
    

except Exception as e:
    print("Error:", e)

finally:
    # Cerrar el navegador y la conexión a la base de datos
    if 'driver' in locals():
     mysql_engine.dispose()
