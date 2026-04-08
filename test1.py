import requests
from bs4 import BeautifulSoup
import time

# 要爬的股票
stocks = ["1101", "2330", "1102"]

for stockid in stocks:
    try:
        # Yahoo 股市網址
        url = f"https://tw.stock.yahoo.com/quote/{stockid}.TW"

        headers = {
            "User-Agent": "Mozilla/5.0"
        }

        r = requests.get(url, headers=headers)
        soup = BeautifulSoup(r.text, "html.parser")

        # 抓股價（比較穩的寫法）
        price_tag = soup.find("fin-streamer", {"data-field": "regularMarketPrice"})

        if price_tag:
            price = price_tag.text
        else:
            price = "抓不到"

        message = f"📈 股票 {stockid}\n💰 即時股價：{price}"

        # Telegram 設定
        token = "你的BOT_TOKEN"
        chat_id = "你的CHAT_ID"

        tg_url = f"https://api.telegram.org/bot{token}/sendMessage"
        data = {
            "chat_id": chat_id,
            "text": message
        }

        requests.post(tg_url, data=data)

        time.sleep(3)

    except Exception as e:
        print(f"{stockid} 發生錯誤:", e)
