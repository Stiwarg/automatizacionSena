import sys
import shutil
import os
import subprocess

def move_file_to_documents(ruta_file):
    # Ruta de la carpeta de documentos en el proyecto de Python
    #document_folder_path = 'C:\\Users\\SENA\\Desktop\\bot\\bots\\documentos'
    document_folder_path = 'C:\\xampp\htdocs\\automatizacionSena\\bots\\documentos'

    try:
        # Obtener el nombre del archivo
        name_file = os.path.basename(ruta_file)

        # Mover el archivo Excel a la carpeta documentos
        shutil.move(ruta_file, os.path.join(document_folder_path, name_file))
        print("Archivo movido correctamente a la carpeta de documentos.")

        # Verificar y ejecutar el script Python correspondiente
        if "CONTRATISTAS_2024_BD" in name_file:
            log_message = "Archivo de contratistas: " + name_file
            subprocess.call(["python", "C:\\xampp\\htdocs\\automatizacionSena\\bots\\contratistasBaseD.py"], shell=True)
            #subprocess.call(["python", "C:\\xampp\\htdocs\\bots\\contratistasBaseD.py"], shell=True)
        elif "INSTRUCTORES_AREA_CONTRATISTA" in name_file:
            log_message = "Archivo de instructores de área contratista: " + name_file
            subprocess.call(["python", "C:\\xampp\\htdocs\\automatizacionSena\\bots\\contratistasArea.py"], shell=True)
            #subprocess.call(["python", "C:\\xampp\\htdocs\\bots\\contratistaArea.py"], shell=True)
        elif "Instructores_AREA" in name_file:
            log_message = "Archivo de instructores de área: " + name_file
            subprocess.call(["python", "C:\\xampp\\htdocs\\automatizacionSena\\bots\\areaPlanta.py"], shell=True)
            #subprocess.call(["python", "C:\\xampp\\htdocs\\bots\\areaPlanta.py"], shell=True)
        elif "PLANTA_2024_BD" in name_file:
            log_message = "Archivo de planta: " + name_file
            subprocess.call(["python", "C:\\xampp\\htdocs\\automatizacionSena\\bots\\plantaBaseD.py"], shell=True)
            #subprocess.call(["python", "C:\\xampp\\htdocs\\bots\\plantaBaseD.py"], shell=True)
        else:
            log_message = "Nombre de archivo no reconocido: " + name_file

        # Escribir el mensaje de registro en el archivo debug_log.txt
        #with open("C:\\Users\\SENA\\Desktop\\bot\\bots\\debug_log.txt", "a") as log_file:
        #   log_file.write(log_message + "\n")

        with open("C:\\xampp\\htdocs\\automatizacionSena\\bots\\debug_log.txt", "a") as log_file:
            log_file.write(log_message + "\n")
    except Exception as e:
        print("Error al mover o ejecutar el archivo:", str(e))

if __name__ == '__main__':
    # Verificar si se proporcionó una ruta de archivo como argumento
    if len(sys.argv) > 1:
        # Obtener la ruta del archivo de Excel
        excel_file = sys.argv[1]

        # Procesar el archivo de Excel
        move_file_to_documents(excel_file)
