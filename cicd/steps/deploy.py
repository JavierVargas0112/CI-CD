import os
import subprocess
import sys
import time
import urllib.request

app = os.environ["APP"]
version = os.environ["VERSION"]
port = os.environ["PORT"]
health_url = os.environ["HEALTH_URL"]

# 1. La versión que está en marcha pasa a ser "previous" (para el rollback)
exists = subprocess.run(["docker", "image", "inspect", f"{app}:current"],
                        capture_output=True)
if exists.returncode == 0:
    subprocess.run(["docker", "tag", f"{app}:current", f"{app}:previous"])

# 2. La versión nueva pasa a ser "current"
result = subprocess.run(["docker", "tag", f"{app}:{version}", f"{app}:current"])
if result.returncode != 0:
    print(f"ERROR: no existe la imagen {app}:{version}")
    sys.exit(10)

# 3. Parar y borrar el contenedor anterior
subprocess.run(["docker", "rm", "-f", app])

# 4. Arrancar la versión nueva
result = subprocess.run(["docker", "run", "-d", "--name", app,
                         "-p", f"{port}:8080", f"{app}:current"])
if result.returncode != 0:
    print("ERROR: el contenedor no ha podido arrancar")
    sys.exit(11)

# 5. Healthcheck: esperar a que la aplicación responda (máximo 60 s)
for attempt in range(60):
    try:
        urllib.request.urlopen(health_url, timeout=2)
        print(f"La aplicación responde en {health_url}")
        sys.exit(0)
    except Exception:
        time.sleep(1)

print("ERROR: la aplicación no responde")
sys.exit(12)