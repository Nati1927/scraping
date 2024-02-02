from bs4 import BeautifulSoup
import requests
import io
import sys
import time

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

bot_token = '6050967264:AAGwCgmE-FIwwd4QZBRlOmnpXMrYUqpXsAY'
chat_id = 6721816560

response = requests.get('https://helloomarket.com/')
soup = BeautifulSoup(response.text, 'html.parser')
products = soup.find_all('div', class_='product-item')

def send_to_telegram(bot_token, chat_id, text):
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    params = {
        'chat_id': chat_id,
        'text': text
    }
    response = requests.post(url, params=params)
    return response.json()

for product in products:
    title = product.find('h2', class_='product-title').get_text(strip=True)
    price = product.find('span', class_='price').get_text(strip=True)
    link = product.find('a', href=True)['href']

    text = f"Product: {title}\nPrice: {price}\nLink: https://helloomarket.com{link}\n"
    response = send_to_telegram(bot_token, chat_id, text)
    print(response)
    time.sleep(30)
