import csv
import os
import shutil
import subprocess
import sys
from pathlib import Path

project = Path(os.environ["PROJECT_DIR"])
# Cobertura mínima de líneas, por ejemplo 0.50 = 50 % (si no está en el .env, se usa la del pom.xml)
minimum = os.environ.get("COVERAGE_MIN")

# 1. ¿Se ha generado el fichero de ejecución de JaCoCo en test.py?
if not (project / "target" / "jacoco.exec").exists():
    print("ERROR: target/jacoco.exec not found, run the tests first")
    sys.exit(2)

# 2. Generar el informe (HTML en target/site/jacoco/index.html + CSV)
mvn = shutil.which("mvn")
result = subprocess.run([mvn, "-B", "jacoco:report"], cwd=project)
if result.returncode != 0:
    print("ERROR: jacoco:report failed")
    sys.exit(result.returncode)

# 3. Mostrar el porcentaje de líneas cubiertas en el log
covered = missed = 0
with open(project / "target" / "site" / "jacoco" / "jacoco.csv", encoding="utf-8") as f:
    for row in csv.DictReader(f):
        covered += int(row["LINE_COVERED"])
        missed += int(row["LINE_MISSED"])
total = covered + missed
print(f"Line coverage: {covered}/{total} = {100 * covered / total if total else 0:.1f}%")

# 4. Comprobar que se llega al mínimo (falla si no)
command = [mvn, "-B", "jacoco:check"]
if minimum:
    command.append(f"-Djacoco.min.coverage={minimum}")
result = subprocess.run(command, cwd=project)
sys.exit(result.returncode)
