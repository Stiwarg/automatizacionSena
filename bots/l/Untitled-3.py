import pandas as pd
from sqlalchemy import create_engine

# Leer los archivos Excel y especificar la tabla de destino para cada uno
excel_files = {
    'C:\\Users\\SENA\\Desktop\\bot\\documentos\\Datos_Contratistas_2024.xlsx': 'instructores',
    # 'C:/Users/loitt/Escritorio/Nueva carpeta/Datos_Contratistas_2024.xlsx': 'failed_jobs',
    # 'archivo2.xlsx': 'tabla2',
}

# Configurar la conexión a la base de datos MySQL en PhpMyAdmin
mysql_engine = create_engine('mysql+mysqlconnector://root:@localhost/proyecto')

try:
    # Iterar sobre cada archivo Excel y tabla de destino
    for excel_file, table in excel_files.items():
        # Leer el archivo Excel
        df = pd.read_excel(excel_file)
        
        # Insertar los datos en la tabla correspondiente en la base de datos MySQL
        df.to_sql(table, con=mysql_engine, if_exists='replace', index=False)

        print(f"Datos insertados correctamente en la tabla {table}.")
except Exception as e:
    print("Error al insertar datos en la base de datos:", e)
finally:
    # Cerrar la conexión
    mysql_engine.dispose()
