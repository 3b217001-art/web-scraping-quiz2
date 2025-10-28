
# 1. scrape1.py

執行要求：

使用 requests 套件發送 GET 請求到目標網站，並取得網頁的 HTML 原始碼 (字串)。
撰寫一個正規表示式樣板 (Pattern)，用來匹配頁面上所有書籍的價格。
提示：價格格式固定為：£ + 數字 + . + 兩位數字
使用 re.findall() 方法，從 HTML 原始碼中找出所有符合價格格式的字串。
程式執行後，直接在終端機 (Terminal) 印出一個包含所有價格字串的 Python 列表 (List)。

預期輸出範例：

['£45.17', '£49.43', '£48.87', '£36.94', '£37.33', '£44.34', '£30.54', '£56.88', '£23.21', '£38.95', '£26.08']

# 2. scrape1.py

執行要求：

使用 requests 取得網頁內容，並使用 BeautifulSoup 與 lxml 解析器建立 Soup 物件。
定位到頁面上所有書籍的容器。
提示：每本書的資訊都包在一個 <article class="product_pod"> 標籤內。
遍歷 (Loop) 每一本書的容器，並從中擷取以下三項資訊：
書名 (Title)：
提示：在 <h3> 標籤內的 <a> 標籤中。請擷取 <a> 標籤的 title 屬性。
價格 (Price)：
提示：在 <p class="price_color"> 標籤內。
評分 (Rating)：
提示：評分資訊藏在 <p> 標籤的 class 屬性中，例如 <p class="star-rating Three"> 代表 3 顆星。你需要擷取出 Three, Five, One 等文字。
評分的 class 名稱格式為 "star-rating [Rating]"，其中 [Rating] 可能是：One, Two, Three, Four, Five
需要從 class 屬性中提取第二個值（評分文字）
建議使用 .get() 方法安全地取得屬性值
將每本書的資訊整理成一個 Python 字典 (Dictionary)。
最後，將所有書本的字典加入一個列表 (List) 中。
程式執行後，在終端機將這個最終的列表印出，並輸出成 json。

預期輸出範例：


[
  {
    "title": "It's Only the Himalayas",
    "price": "£45.17",
    "rating": "Two"
  },
  {
    "title": "Full Moon over Noahâs Ark: An Odyssey to Mount Ararat and Beyond",
    "price": "£49.43",
    "rating": "Four"
  },
  {
    "title": "See America: A Celebration of Our National Parks & Treasured Sites",
    "price": "£48.87",
    "rating": "Three"
  },
  ...
  ...
  ...
  {
    "title": "1,000 Places to See Before You Die",
    "price": "£26.08",
    "rating": "Five"
  }
]

## 包含的檔案
- `.gitignore`：常見的忽略清單（Python / VS Code / macOS 等）。
- `LICENSE`：採用 MIT 授權（請將作者與年份修改為適當內容）。
- `README.md`：此說明檔。
