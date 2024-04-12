import sys
import shutil
import os
import subprocess

def move_file_to_documents_excels(ruta_file):
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
        if "ReportedeJuiciosEvaluativos_" in name_file:
            subprocess.call(["python", "C:\\xampp\\htdocs\\automatizacionSena\\bots\\juiciosEvaluativosBaseD.py"], shell=True)
            #subprocess.call(["python", "C:\\xampp\\htdocs\\bots\\juiciosEvaluativosBaseD.py"], shell=True)
            log_message = "Archivo de juicios evaluativos: " + name_file
        else:
            log_message = "Nombre de archivo no reconocido: " + name_file

        # Escribir el mensaje de registro en el archivo debug_log.txt
        #with open("C:\\Users\\SENA\\Desktop\\bot\\bots\\debug_log.txt", "a") as log_file:
        #   log_file.write(log_message + "\n")

        with open("C:\\xampp\\htdocs\\automatizacionSena\\bots\\juice.log.txt", "a") as log_file:
            log_file.write(log_message + "\n")
    except Exception as e:
        print("Error al mover o ejecutar el archivo:", str(e))

if __name__ == '__main__':
    # Verificar si se proporcionó una ruta de archivo como argumento
    if len(sys.argv) > 1:
        # Obtener la ruta del archivo de Excel
        excel_file = sys.argv[1]

        # Procesar el archivo de Excel
        move_file_to_documents_excels(excel_file)
