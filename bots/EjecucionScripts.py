# Contenido de main.py
import subprocess
import time

# Ejecutar script1.py
subprocess.call(["python", "C:/Users/SENA/Desktop/bot/bots/contratistasBaseD.py"])

# Ejecutar script2.py
subprocess.call(["python", "C:/Users/SENA/Desktop/bot/bots/juiciosEvaluativosBaseD.py"])

# Ejecutar script3.py
subprocess.call(["python", "C:/Users/SENA/Desktop/bot/bots/plantaBaseD.py"])

#Ejecutar script4.py
subprocess.call(["python", "C:/Users/SENA/Desktop/bot/bots/reporteAsignacionBaseD.py"])

#Ejecutar script5.py
subprocess.call(["python", "C:/Users/SENA/Desktop/bot/bots/reporteNovedadesBaseD.py"])

#Ejecutar script6.py
subprocess.call(["python", "C:/Users/SENA/Desktop/bot/bots/ReporteNovedadesBaseDa.py"])

#Ejecutar script7.py
subprocess.call(["python", "C:/Users/SENA/Desktop/bot/bots/reporteTituladaBaseD.py"])

time.sleep(60)
#ejecucion de los script de descarga de documentos
subprocess.call(["python","C:/Users/SENA/Desktop/bot/bots/reportefichas.py"])

subprocess.call(["python","C:/Users/SENA/Desktop/bot/bots/asignacionResultados.py"])

subprocess.call(["python","C:/Users/SENA/Desktop/bot/bots/ReporteNovedades.py"])

subprocess.call(["python","C:/Users/SENA/Desktop/bot/bots/TramitesReporte.py"])


