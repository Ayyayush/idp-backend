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

    sample_text = text[:5000]

    prompt = f"""
You are a document classifier.

Classify the document into EXACTLY one category:

Resume
Invoice
Financial Statement
Marksheet
Aadhaar
Other

Rules:

- Educational scorecards should be Marksheet.
- CBSE/ICSE scorecards are Marksheet.
- Exam result sheets are Marksheet.
- Student report cards are Marksheet.
- CVs and resumes are Resume.
- Bills are Invoice.
- Bank statements are Financial Statement.

Return ONLY the category name.

Document:

{sample_text}
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


def answer_question(
    question,
    retrieved_docs
):

    context = "\n".join(
        retrieved_docs
    )

    prompt = f"""
You are a document question answering assistant.

STRICT RULES:

1. Answer ONLY using information present in the provided context.
2. Never guess.
3. Never infer missing information.
4. Never use external knowledge.
5. If the answer is not explicitly present in the context, respond exactly:

I could not find that information in the document.

Context:
{context}

Question:
{question}

Answer:
"""

    response = llm.invoke(
        prompt
    )

    return response.content.strip()