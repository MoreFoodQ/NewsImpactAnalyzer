import requests
from bs4 import BeautifulSoup
from opencc import OpenCC
from openai import OpenAI


# 初始化OpenAI GPT-4
client = OpenAI(api_key='')

def fetch_news(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    title_tag = soup.find('h1', class_='title')
    title = title_tag.text if title_tag else '標題未找到'
    content_tags = soup.find_all('span', class_='richtext-text css-1iqe90x')
    content = '\n'.join([tag.text for tag in content_tags if tag.text]) if content_tags else '內容未找到'
    return title, content

def convert_s2t(text):
    cc = OpenCC('s2t')  # 從簡體到繁體
    return cc.convert(text)

def analyze_impact(news_title, news_content):
    # 使用GPT-4進行市場影響分析
    messages = [{
        "role": "user",
        "content": f"請分析以下新聞標題和內容對市場的可能影響,並且在最後條列式簡介新聞主角的業務內容(若無則不須列),300字內需要精簡：\n標題：{news_title}\n內容：{news_content}\n分析："
    }]
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=0.5,
        max_tokens=300,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )
    return response.choices[0].message.content


def send_telegram_message(chat_id, text, bot_token):
    url = f'https://api.telegram.org/bot{bot_token}/sendMessage'
    payload = {
        'chat_id': chat_id,
        'text': text,
        'parse_mode': 'HTML'
    }
    response = requests.post(url, data=payload)
    print(response.json())

bot_token = ''
chat_id = ''
news_url = ''

# 爬取新聞
title, content = fetch_news(news_url)

# 轉換繁體中文
title = convert_s2t(title)
content = convert_s2t(content)

# 分析新聞對市場的可能影響
impact_analysis = analyze_impact(title, content)

# 消息格式化，增加來源網址和市場影響分析
message = f"<b>{title}</b>\n\n{content}\n\n<b>🕶️經AI分析</b>，{impact_analysis}\n\n來源：<a href='{news_url}'>點擊查看原文</a>"

# 發送消息
send_telegram_message(chat_id, message, bot_token)
