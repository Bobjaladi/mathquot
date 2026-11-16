name: Update daily.json

on:
  schedule:
    - cron: "30 23 * * *"   # 5:00 AM IST every day
  workflow_dispatch:         # lets you run it manually from the Actions tab

permissions:
  contents: write            # needed so the action can push the commit

jobs:
  update-daily:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout repo
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.12"

      - name: Copy temp_daily.json to daily.json
        run: python copy_daily.py

      - name: Commit and push if changed
        run: |
          git config user.name "github-actions[bot]"
          git config user.email "github-actions[bot]@users.noreply.github.com"
          git add daily.json
          if git diff --cached --quiet; then
            echo "No changes to commit."
          else
            git commit -m "Daily update $(TZ=Asia/Kolkata date +'%Y-%m-%d')"
            git push
          fi
