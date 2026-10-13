import os
import shutil
import subprocess
import sys

project = os.environ["PROJECT_DIR"]
# Nombre de la imagen: nombre de la app + versión, por ejemplo jolienom:a1b2c3d
image = f"{os.environ['APP']}:{os.environ['VERSION']}"

# 1. Generar el .jar (los tests ya se han pasado en test.py)
mvn = shutil.which("mvn")
result = subprocess.run([mvn, "-B", "package", "-DskipTests"], cwd=project)
if result.returncode != 0:
    print("ERROR: mvn package failed")
    sys.exit(result.returncode)

# 2. Construir la imagen Docker con ese .jar
result = subprocess.run(["docker", "build", "-t", image, "."], cwd=project)
sys.exit(result.returncode)