# Contenido de main.py
import subprocess
import time
# Lista de scripts a ejecutar
scripts = [
    "C:/xampp/htdocs/automatizacionSena/bots/reportefichas.py",
    "C:/xampp/htdocs/automatizacionSena/bots/asignacionResultados.py",
    "C:/xampp/htdocs/automatizacionSena/bots/ReporteNovedades.py",
    "C:/xampp/htdocs/automatizacionSena/bots/TramitesReporte.py"
]

for script in scripts:
    process = subprocess.Popen(["python", script])
    # Espera un tiempo máximo de 60 segundos para que el proceso termine
    try:
        process.wait(timeout=60)
    except subprocess.TimeoutExpired:
        print("El proceso ha tardado demasiado en finalizar.")

time.sleep(30)
#ejecucion script subida en base de datos
subprocess.call(["python", "C:/xampp/htdocs/automatizacionSena/bots/areaPlanta.py"])
time.sleep(10)
subprocess.call(["python", "C:/xampp/htdocs/automatizacionSena/bots/contratistasArea.py"])
time.sleep(10)
subprocess.call(["python", "C:/xampp/htdocs/automatizacionSena/bots/contratistasBaseD.py"])
time.sleep(10)
subprocess.call(["python", "C:/xampp/htdocs/automatizacionSena/bots/juiciosEvaluativosBaseD.py"])
time.sleep(10)
subprocess.call(["python", "C:/xampp/htdocs/automatizacionSena/bots/plantaBaseD.py"])
time.sleep(10)
subprocess.call(["python", "C:/xampp/htdocs/automatizacionSena/bots/reporteAsignacionBaseD.py"])
time.sleep(10)
subprocess.call(["python", "C:/xampp/htdocs/automatizacionSena/bots/reporteNovedadesBaseD.py"])
time.sleep(10)
subprocess.call(["python", "C:/xampp/htdocs/automatizacionSena/bots/ReporteNovedadesBaseDa.py"])
time.sleep(10)
subprocess.call(["python", "C:/xampp/htdocs/automatizacionSena/bots/reporteTituladaBaseD.py"])
time.sleep(10)
subprocess.call(["python", "C:/xampp/htdocs/automatizacionSena/bots/excels.py"])
#time.sleep(10)
#subprocess.call(["python", "C:/xampp/htdocs/automatizacionSena/bots/EnviosCorreos.py"])
#time.sleep(10)
#subprocess.call(["python", "C:/xampp/htdocs/automatizacionSena/bots/TercerCorreo.py"])

