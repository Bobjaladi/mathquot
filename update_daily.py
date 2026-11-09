import json
import os
from datetime import datetime

# ─── Configuration ───────────────────────────────────────────────
TEMP_FILE = "temp_daily.json"   # You edit this file manually
DAILY_FILE = "daily.json"       # GitHub updates this automatically at 5:00 AM

def main():
    # 1. Check if temp file exists
    if not os.path.exists(TEMP_FILE):
        print(f"❌ Error: {TEMP_FILE} not found! Please create it first.")
        return

    # 2. Load the data from temp_daily.json
    with open(TEMP_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)

    # 3. Add an official "published" timestamp (optional but recommended)
    if isinstance(data, list):
        # If your temp file is just an array [...], wrap it nicely
        final_data = {
            "date": datetime.now().strftime("%Y-%m-%d"),
            "published_at": datetime.now().isoformat(),
            "questions": data
        }
    else:
        # If your temp file is already an object {...}, just add the timestamp
        data["published_at"] = datetime.now().isoformat()
        data["date"] = datetime.now().strftime("%Y-%m-%d")
        final_data = data

    # 4. Save it to daily.json
    with open(DAILY_FILE, "w", encoding="utf-8") as f:
        json.dump(final_data, f, indent=2, ensure_ascii=False)
        
    print(f"✅ Successfully published {TEMP_FILE} to {DAILY_FILE}")

if __name__ == "__main__":
    main()
