import os
import re
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

PROMPT = """
Ты профессиональный маркетолог и копирайтер.

Сделай:
1. Короткое описание
2. 5 преимуществ
3. 2 слогана
4. Хештеги

Пиши аккуратно, с абзацами и переносами строк.
Без Markdown.
"""

def clean(text: str) -> str:
    return re.sub(r"[`*]", "", text)

def stream_marketing(product: str):
    with client.responses.stream(
        model="gpt-5.2",
        instructions=PROMPT,
        input=f"Товар: {product}",
    ) as stream:
        for event in stream:
            if event.type == "response.output_text.delta":
                yield clean(event.delta)
