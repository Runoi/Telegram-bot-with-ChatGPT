from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv('key.env')  # Загружает переменные из .env
api_key = os.getenv('CHATGPT_API_KEY')

# Выбираем модель GPT
GPT_MODEL = "gpt-3.5-turbo"

