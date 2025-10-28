import re
import requests

URL = "https://books.toscrape.com/catalogue/category/books/travel_2/index.html"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36'
}
try:
    response = requests.get(URL, headers=headers, timeout=10)
    response.raise_for_status()
    response.encoding = 'utf-8' # 確保中文內容正確解碼 # type: ignore

    # 描述書的價格的正規表示式
    price_pattern = re.compile(r'£\d+\.\d{2}')
    # 尋找所有 價格格
    prices = re.findall(price_pattern, response.text)
    # 測試用
    # for price in prices:
    #   print(price)
    # 建立一個包含所有價格字串的列表
    price_list = [f"{price}" for price  in prices] # type: ignore
    print(f"{price_list}")
    # ['£45.17', '£49.43', '£48.87', '£36.94', '£37.33', '£44.34', '£30.54', '£56.88', '£23.21', '£38.95', '£26.08']

except requests.exceptions.RequestException as e:
    print(f"爬取失敗: {e}") # type: ignore