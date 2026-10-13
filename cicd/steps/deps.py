import os
import shutil
import subprocess
import sys

# Busca Maven (en Windows es mvn.cmd)
mvn = shutil.which("mvn")

# Descarga todas las dependencias del proyecto
result = subprocess.run([mvn, "-B", "dependency:go-offline"],
                        cwd=os.environ["PROJECT_DIR"])

# Termina con el mismo código que Maven: 0 si todo ha ido bien
sys.exit(result.returncode)