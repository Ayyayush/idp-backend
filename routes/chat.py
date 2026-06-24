from fastapi import APIRouter
from pydantic import BaseModel

from services.chroma_service import search_document
from services.llm_service import answer_question

router = APIRouter()


class ChatRequest(BaseModel):
    question: str


@router.post("/chat")
async def chat_document(
    request: ChatRequest
):

    retrieved_docs = search_document(
        request.question
    )

    documents = retrieved_docs["documents"][0]

    if not documents:
     return {
        "question": request.question,
        "answer": "No relevant information found in the document."
     }

    answer = answer_question(
        request.question,
        documents
    )

    return {
        "question": request.question,
        "answer": answer
    }