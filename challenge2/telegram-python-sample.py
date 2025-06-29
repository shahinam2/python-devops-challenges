import requests
from dotenv import load_dotenv
import os

load_dotenv()

bot_token = os.getenv('TELEGRAM_BOT_TOKEN')
chat_id = os.getenv('TELEGRAM_CHAT_ID')
message = 'Hello from Python!'

url = f'https://api.telegram.org/bot{bot_token}/sendMessage'
payload = {'chat_id': chat_id, 'text': message}

response = requests.post(url, data=payload)
print(response.json())