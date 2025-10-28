import requests
from bs4 import BeautifulSoup
import json

# 使用 lxml 解析器 (推薦：速度快、容錯性強)
try:
    response = requests.get("https://books.toscrape.com/catalogue/category/books/travel_2/index.html")
    response.encoding = 'utf-8'
    response.raise_for_status()  # 確保請求成功
    # 1.用 BeautifulSoup 解析 
    soup_lxml = BeautifulSoup(response.text, 'lxml')
    # print("--- 使用 lxml 解析成功 ---")
    # print(soup_lxml.prettify()) # prettify() 可美化輸出，方便除錯
    # 2. find_all(tag, attributes, recursive, string, limit, kwargs)
    book_containers = soup_lxml.find_all('article', class_='product_pod')
    # 測試 print(f"這一頁共有 {len(book_containers)} 本書\n")

    books = []

    # 3. 迴圈 (Loop)
    for book in book_containers:
        # 書名
        title_tag = book.find('h3').find('a')
        title = title_tag.get("title", "無標題")

        # 價格
        price = book.find('p', class_='price_color').text  # 取得價格
        # print(f"書名: {title}, 價格: {price}") 
        # 評分
        rating_tag = book.find("p", class_="star-rating")
        rating_class = rating_tag.get("class", [])
        # class 是一個 list，例如 ["star-rating", "Three"]
        # rating_class = rating_tag.get("class", []) if rating_tag else []
        rating = rating_class[1] if len(rating_class) > 0 else "無評分"

        # 加入書本字典
        books.append({
            "title": title,
            "price": price,
            "rating": rating
        })

    #    JSON 格式
    print(json.dumps(books, ensure_ascii=False, indent=2))

except requests.RequestException as e:
    print(f"網路請求失敗: {e}")