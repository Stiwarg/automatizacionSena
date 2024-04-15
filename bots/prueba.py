import subprocess
import time

# Lista de scripts a ejecutar
scripts = [
    "C:/xampp/htdocs/automatizacionSena/bots/reportefichas.py",
    "C:/xampp/htdocs/automatizacionSena/bots/asignacionResultados.py",
    "C:/xampp/htdocs/automatizacionSena/bots/ReporteNovedades.py",
    "C:/xampp/htdocs/automatizacionSena/bots/TramitesReporte.py"
]

# Ejecutar los primeros scripts de la lista
for script in scripts:
    print(f"Ejecutando el script: {script}")
    process = subprocess.Popen(["python", script])
    try:
        # Esperar un tiempo máximo de 60 segundos para que el proceso termine
        process.wait(timeout=60)
        print(f"El script {script} ha finalizado correctamente.")
    except subprocess.TimeoutExpired:
        print(f"El script {script} ha tardado demasiado en finalizar.")
    except Exception as e:
        print(f"Se ha producido un error al ejecutar el script {script}: {e}")

# Esperar 10 segundos antes de ejecutar los siguientes scripts
time.sleep(60)

# Lista de scripts adicionales
otros_scripts = [
    "areaPlanta.py",
    "contratistasArea.py",
    "contratistasBaseD.py",
    "juiciosEvaluativosBaseD.py",
    "plantaBaseD.py",
    "reporteAsignacionBaseD.py",
    "reporteNovedadesBaseD.py",
    "ReporteNovedadesBaseDa.py",
    "reporteTituladaBaseD.py",
]

# Ejecutar los scripts adicionales
for script in otros_scripts:
    print(f"Ejecutando el script: {script}")
    process = subprocess.Popen(["python", f"C:/xampp/htdocs/automatizacionSena/bots{script}"])
    try:
        # Esperar un tiempo máximo de 60 segundos para que el proceso termine
        process.wait(timeout=60)
        print(f"El script {script} ha finalizado correctamente.")
    except subprocess.TimeoutExpired:
        print(f"El script {script} ha tardado demasiado en finalizar.")
    except Exception as e:
        print(f"Se ha producido un error al ejecutar el script {script}: {e}")
