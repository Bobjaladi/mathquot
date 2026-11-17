import json
import shutil
import sys

SRC = "temp_daily.json"
DST = "daily.json"

# Make sure the source is valid JSON before publishing it
try:
    with open(SRC, "r", encoding="utf-8") as f:
        json.load(f)
except Exception as e:
    print(f"❌ {SRC} is missing or invalid: {e}")
    sys.exit(1)

shutil.copyfile(SRC, DST)
print(f"✅ Copied {SRC} to {DST}")
