name: Stock Bot

on:
  schedule:
    - cron: "*/5 * * * *"   # 每5分鐘
  workflow_dispatch:

jobs:
  run-bot:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v3

      - name: Install Python
        uses: actions/setup-python@v4
        with:
          python-version: 3.10

      - name: Install dependencies
        run: pip install requests beautifulsoup4

      - name: Run script
        run: python stock_bot.py
