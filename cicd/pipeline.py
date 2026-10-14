import os
import subprocess
import sys
import time
from datetime import datetime
from pathlib import Path
from dotenv import dotenv_values

# --- Configuración ---
BASE = Path(__file__).resolve().parent              # carpeta cicd
STEPS = ["check", "deps", "build", "test", "coverage", "package", "deploy"]

# Lee el .env y lo convierte en diccionario: {"APP": "jolienom", ...}
CONFIG = dotenv_values(BASE / ".env")

# La versión no va en el .env: se calcula a partir del último commit
CONFIG["VERSION"] = subprocess.run(
    ["git", "-C", CONFIG["PROJECT_DIR"], "rev-parse", "--short", "HEAD"],
    capture_output=True, text=True,
).stdout.strip()

# Un fichero de log nuevo en cada ejecución
(BASE / "logs").mkdir(exist_ok=True)
LOG_FILE = BASE / "logs" / f"pipeline_{datetime.now():%Y%m%d_%H%M%S}.log"


def log(level, message):
    """Escribe un mensaje en pantalla y en el fichero de log."""
    line = f"[{datetime.now():%Y-%m-%d %H:%M:%S}] [{level}] {message}"
    print(line)
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(line + "\n")


def run_step(name):
    """Ejecuta steps/<name>.py y devuelve su exit code."""
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        result = subprocess.run([sys.executable, BASE / "steps" / f"{name}.py"],
                                stdout=f, stderr=subprocess.STDOUT,
                                env={**os.environ, **CONFIG})
    return result.returncode


def rollback():
    """Vuelve a poner en marcha la versión anterior."""
    log("WARN", "Starting rollback")
    if run_step("rollback") == 0:
        log("OK", "Rollback completed")
    else:
        log("ERROR", "Rollback failed")


def main():
    for step in STEPS:
        log("INFO", f"Starting: {step}")
        start = time.time()
        code = run_step(step)

        if code == 0:
            log("OK", f"{step} finished in {time.time() - start:.0f}s")
        else:
            log("ERROR", f"{step} failed with exit code {code}")
            if step == "deploy":
                rollback()
            sys.exit(code)

    log("OK", "Pipeline finished successfully")


if __name__ == "__main__":
    main()