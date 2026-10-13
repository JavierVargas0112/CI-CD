import os
import subprocess
import sys

app = os.environ["APP"]
port = os.environ["PORT"]

# 1. ¿Existe una versión anterior a la que volver?
check = subprocess.run(["docker", "image", "inspect", f"{app}:previous"],
                       capture_output=True)
if check.returncode != 0:
    print("ERROR: no previous version to roll back to")
    sys.exit(2)

# 2. Parar y borrar el contenedor que ha fallado
subprocess.run(["docker", "rm", "-f", app])

# 3. La versión anterior vuelve a ser la actual
subprocess.run(["docker", "tag", f"{app}:previous", f"{app}:current"])

# 4. Arrancarla
result = subprocess.run(["docker", "run", "-d", "--name", app,
                         "-p", f"{port}:8080", f"{app}:current"])
sys.exit(result.returncode)