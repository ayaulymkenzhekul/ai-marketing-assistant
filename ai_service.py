from openai import OpenAI
import os
from dotenv import load_dotenv
import re

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

PROMPT_MARKETING = """
Ты профессиональный маркетолог и копирайтер.
Сделай маркетинговое описание товара.

Нужно:
Короткое описание
5 преимуществ
2 слогана
Хештеги

Стиль: продающий.
Без Markdown. Без символов # и *.
Только обычный текст.

Товар:
"""

def clean(text):
    return re.sub(r'[#*`-]', '', text)

def generate_marketing(product):
    response = client.chat.completions.create(
        model="gpt-4.1-mini",  
        messages=[
            {"role": "user", "content": PROMPT_MARKETING + product}
        ]
    )
    return clean(response.choices[0].message.content)
