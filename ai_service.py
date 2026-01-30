from openai import OpenAI
import os
from dotenv import load_dotenv
import re

from openai.types.shared.reasoning import Reasoning

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
"""


def clean(text):
    return re.sub(r"[#*`-]", "", text)


def generate_marketing(product):
    try:
        response = client.responses.create(
            model="gpt-5.2",
            reasoning=Reasoning(effort="low"),
            instructions=PROMPT_MARKETING,
            input="Товар: " + product,
        )
        return clean(response.output_text)
    except Exception as e:
        return f"Ошибка при генерации маркетингового описания: {e}"
