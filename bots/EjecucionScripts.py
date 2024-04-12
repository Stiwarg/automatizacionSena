# Contenido de main.py
import subprocess
import time
# Lista de scripts a ejecutar
scripts = [
    "C:/Users/SENA/Desktop/bot/bots/reportefichas.py",
    "C:/Users/SENA/Desktop/bot/bots/asignacionResultados.py",
    "C:/Users/SENA/Desktop/bot/bots/ReporteNovedades.py",
    "C:/Users/SENA/Desktop/bot/bots/TramitesReporte.py"
]

for script in scripts:
    process = subprocess.Popen(["python", script])
    # Espera un tiempo máximo de 60 segundos para que el proceso termine
    try:
        process.wait(timeout=20)
    except subprocess.TimeoutExpired:
        print("El proceso ha tardado demasiado en finalizar.")

time.sleep(10)
#ejecucion script subida en base de datos
subprocess.call(["python", "C:/Users/SENA/Desktop/bot/bots/areaPlanta.py"])
time.sleep(10)
subprocess.call(["python", "C:/Users/SENA/Desktop/bot/bots/contratistasArea.py"])
time.sleep(10)
subprocess.call(["python", "C:/Users/SENA/Desktop/bot/bots/contratistasBaseD.py"])
time.sleep(10)
subprocess.call(["python", "C:/Users/SENA/Desktop/bot/bots/juiciosEvaluativosBaseD.py"])
time.sleep(10)
subprocess.call(["python", "C:/Users/SENA/Desktop/bot/bots/plantaBaseD.py"])
time.sleep(10)
subprocess.call(["python", "C:/Users/SENA/Desktop/bot/bots/reporteAsignacionBaseD.py"])
time.sleep(10)
subprocess.call(["python", "C:/Users/SENA/Desktop/bot/bots/reporteNovedadesBaseD.py"])
time.sleep(10)
subprocess.call(["python", "C:/Users/SENA/Desktop/bot/bots/ReporteNovedadesBaseDa.py"])
time.sleep(10)
subprocess.call(["python", "C:/Users/SENA/Desktop/bot/bots/reporteTituladaBaseD.py"])
time.sleep(10)
subprocess.call(["python", "C:/Users/SENA/Desktop/bot/bots/excels.py"])
time.sleep(10)
subprocess.call(["python", "C:/Users/SENA/Desktop/bot/bots/EnviosCorreos.py"])
time.sleep(10)
subprocess.call(["python", "C:/Users/SENA/Desktop/bot/bots/TercerCorreo.py"])

