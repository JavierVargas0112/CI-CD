from pathlib import Path
from dotenv import dotenv_values
import subprocess



BASE = Path(__file__).resolve().parent
STEPS = ["check", "deps", "build", "test", "package", "deploy"]

CONFIG = dotenv_values(BASE / ".env")
CONFIG["VERSION"] = subprocess.run(
    ["git", "-C", CONFIG["PROJECT_DIR"], "rev-parse", "--short", "HEAD"],
    capture_output=True, text=True,
).stdout.strip()

#Logs
(BASE / "logs").mkdir(exist_ok=True)




