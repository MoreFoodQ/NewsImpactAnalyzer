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

<pre> pip install requests beautifulsoup4 opencc-python-reimplemented openai  </pre> 

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
許可證
本項目採用 MIT 許可證，詳情請見 LICENSE 文件。
