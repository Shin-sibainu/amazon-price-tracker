import requests
from bs4 import BeautifulSoup
import time

amazonURL = "https://www.amazon.co.jp/Python%E3%81%A7%E3%81%AF%E3%81%98%E3%82%81%E3%82%8B%E6%A9%9F%E6%A2%B0%E5%AD%A6%E7%BF%92-%E2%80%95scikit-learn%E3%81%A7%E5%AD%A6%E3%81%B6%E7%89%B9%E5%BE%B4%E9%87%8F%E3%82%A8%E3%83%B3%E3%82%B8%E3%83%8B%E3%82%A2%E3%83%AA%E3%83%B3%E3%82%B0%E3%81%A8%E6%A9%9F%E6%A2%B0%E5%AD%A6%E7%BF%92%E3%81%AE%E5%9F%BA%E7%A4%8E-Andreas-C-Muller/dp/4873117984/ref=sr_1_3?__mk_ja_JP=%E3%82%AB%E3%82%BF%E3%82%AB%E3%83%8A&keywords=python+%E3%82%AA%E3%83%A9%E3%82%A4%E3%83%AA%E3%83%BC&qid=1638589243&sr=8-3"


def amazonTrackingPrice():
    amazonPage = requests.get(amazonURL)
    soup = BeautifulSoup(amazonPage.content, "html.parser")
    # print(soup)

    title = soup.find(id="productTitle").get_text()
    price = soup.find("span", class_="a-size-base").get_text()
    convertedPrice = price[1:6].replace(",", "")
    intPrice = int(convertedPrice)
    print(title)
    print(price)
    print(convertedPrice)

    if(intPrice < 3000):
        sendLineNotify()


def sendLineNotify():
    print("lineに通知がいきました")
    lineNotifyToken = "あなたのLineNotifyトークン"
    lineNotifyApi = "https://notify-api.line.me/api/notify"
    headers = {"Authorization": f"Bearer {lineNotifyToken}"}
    data = {"message": "今がお買い時です！https://www.amazon.co.jp/Python%E3%81%A7%E3%81%AF%E3%81%98%E3%82%81%E3%82%8B%E6%A9%9F%E6%A2%B0%E5%AD%A6%E7%BF%92-%E2%80%95scikit-learn%E3%81%A7%E5%AD%A6%E3%81%B6%E7%89%B9%E5%BE%B4%E9%87%8F%E3%82%A8%E3%83%B3%E3%82%B8%E3%83%8B%E3%82%A2%E3%83%AA%E3%83%B3%E3%82%B0%E3%81%A8%E6%A9%9F%E6%A2%B0%E5%AD%A6%E7%BF%92%E3%81%AE%E5%9F%BA%E7%A4%8E-Andreas-C-Muller/dp/4873117984/ref=sr_1_3?__mk_ja_JP=%E3%82%AB%E3%82%BF%E3%82%AB%E3%83%8A&keywords=python+%E3%82%AA%E3%83%A9%E3%82%A4%E3%83%AA%E3%83%BC&qid=1638589243&sr=8-3"}
    requests.post(lineNotifyApi, headers=headers, data=data)


while(True):
    print("トラッキングしました")
    time.sleep(60 * 60)
    amazonTrackingPrice()
