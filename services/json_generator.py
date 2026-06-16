import json

from services.llm_service import ask_llm


def generate_json(
    text,
    document_type
):

    prompt = f"""
    Document Type:
    {document_type}

    Extract all entities.

    Return ONLY JSON.

    {text}
    """

    response = ask_llm(prompt)

    response = (
        response
        .replace("```json", "")
        .replace("```", "")
        .strip()
    )

    try:
        return json.loads(response)

    except Exception:

        return {
            "error": "json_parse_failed",
            "raw_response": response
        }