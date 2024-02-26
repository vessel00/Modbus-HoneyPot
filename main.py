import os
import subprocess
import concurrent.futures

# Comprobar rutas de llamada
ruta_llamada = os.path.abspath(os.getcwd())
ruta_hp_modbus = str(os.getcwd()) + "/src/application/modbus"


#Si es la llamda de ejecución del HP
if ruta_llamada.endswith("Modbus-HoneyPot"):

    #De esta forma podemos añadir llamadas a nuevos HP en caso de necesitarlo
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        executor.submit(lambda: subprocess.run(["python3", "honeypot.py"], cwd=ruta_hp_modbus))