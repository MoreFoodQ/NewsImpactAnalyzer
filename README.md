# NewsImpactAnalyzer
這個項目是一個自動化新聞爬蟲和分析系統，它能夠從網絡上抓取新聞內容，自動將其從簡體中文轉換為繁體中文，並利用 OpenAI 的 GPT-4 模型進行市場影響分析，最後將分析結果通過 Telegram 發送。

# 新聞爬蟲與分析系統

這個項目是一個自動化新聞爬蟲和分析系統，它能夠從網絡上抓取新聞內容，自動將其從簡體中文轉換為繁體中文，並利用 OpenAI 的 GPT-4 模型進行市場影響分析，最後將分析結果通過 Telegram 發送。

## 功能特點

- **新聞抓取**：從指定的新聞網站抓取新聞標題和內容。
- **語言轉換**：將新聞內容從簡體中文轉換為繁體中文。
- **內容分析**：使用 OpenAI 的 GPT-4 模型分析新聞的市場影響。
- **自動通知**：將新聞和分析結果通過 Telegram 機器人自動發送給用戶。

## 安裝指南

1. 克隆庫：

 <pre>  git clone https://github.com/MoreFoodQ/NewsImpactAnalyzer.git </pre> 

 2. 安裝依賴項：

<pre> pip install beautifulsoup4 opencc-python-reimplemented openai  </pre> 

設定環境變數：  

**OPENAI_API_KEY**：你的 OpenAI API 密鑰。  
**TELEGRAM_BOT_TOKEN**：你的 Telegram 機器人 token。  
**TELEGRAM_CHAT_ID**：要發送消息的 Telegram 聊天 ID。  

使用方法
運行 main.py 文件以啟動爬蟲、進行新聞內容分析和發送結果。你需要修改腳本中的 news_url 以指向你想要抓取的新聞網址。

貢獻指南
歡迎對本項目進行貢獻！你可以透過以下方式幫助改進本項目：

提交 Pull Request 來增加新功能或修復錯誤。
提交 Issue 來報告錯誤或討論改進方向。

**以下為範例:**  
參考新聞網址:https://hk.investing.com/news/stock-market-news/article-701450  

**輸出結果(GPT4o):**  

### 標題: 聯儲局12月降息預期大幅升溫 韓股、日股回暖 施羅德看好亞洲股市

### 影響分析:
- **降息預期提升**: 美國聯儲局預期在12月降息，這通常會對股市產生正面影響，因為降息有助於降低企業借貸成本和增加經濟活動。
- **亞太股市波動**: 日經和韓國KOSPI指數表現強勁，顯示投資者對於降息帶來的利好反應積極。然而，台灣和恒生科技指數的下跌可能反映了市場對其他經濟指標的擔憂。
- **新興市場吸引力增加**: 施羅德的投資官Vis Nayar指出，新興市場的經濟前景和股市估值吸引力正在提升，預計這將吸引更多對高增長潛力感興趣的投資者。

### 業務內容簡介:
- **施羅德投資**: 主要從事資產管理，專注於為全球投資者提供多元化的投資組合，包括股票、債券和其他金融產品。公司近期尤其看好亞洲和新興市場的股票，基於其經濟總體趨勢良好和股市估值具有吸引力。
此次分析展示了降息預期對於提振市場信心的潛在力量，以及對新興市場股票再度燃起興趣的可能性。

### 網址:
[點擊查看原文](https://hk.investing.com/news/stock-market-news/article-701450)


許可證
本項目採用 MIT 許可證，詳情請見 LICENSE 文件。
