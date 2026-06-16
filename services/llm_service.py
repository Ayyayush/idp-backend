import os
import json
import re

from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

llm = ChatGroq(
    api_key=os.getenv("GROQ_API_KEY"),
    model=os.getenv("MODEL_NAME")
)


def classify_document(text):

    prompt = f"""
Classify the following document into one category:

- Invoice
- Resume
- Financial Statement
- Other

Return only the category name.

Document:
{text}
"""

    response = llm.invoke(prompt)

    return response.content.strip()


def extract_entities(text):

    prompt = f"""
Extract all important information from the document.

Return ONLY valid JSON.

Document:
{text}
"""

    response = llm.invoke(prompt)

    content = response.content

    content = re.sub(
        r"```json|```",
        "",
        content
    ).strip()

    try:
        return json.loads(content)

    except Exception:
        return {
            "raw_response": content
        }


def generate_summary(text):

    prompt = f"""
Generate a short professional summary of the document.

Document:
{text}
"""

    response = llm.invoke(prompt)

    return response.content.strip()