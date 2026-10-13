import os
import shutil
import subprocess
import sys
from pathlib import Path

# Carpeta del proyecto Java (la recibe del pipeline.py)
project = Path(os.environ["PROJECT_DIR"])

# 1. ¿Existe el pom.xml?
if not (project / "pom.xml").exists():
    print("ERROR: pom.xml no encontrado en", project)
    sys.exit(2)

# 2. ¿Es un repositorio git?
status = subprocess.run(["git", "status", "--porcelain"],
                        cwd=project, capture_output=True, text=True)
if status.returncode != 0:
    print("ERROR: el proyecto no es un repositorio git")
    sys.exit(3)

# 3. ¿Hay cambios sin commitear?
if status.stdout.strip():
    print("ERROR: hay cambios sin commitear:")
    print(status.stdout)
    sys.exit(4)

# 4. ¿Está Maven instalado?
mvn = shutil.which("mvn")
if mvn is None:
    print("ERROR: Maven no encontrado")
    sys.exit(5)

# 5. ¿El pom.xml es válido?
result = subprocess.run([mvn, "-B", "validate"], cwd=project)
sys.exit(result.returncode)