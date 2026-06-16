from services.llm_service import ask_llm


def generate_summary(text):

    prompt = f"""
    Summarize this document
    in 3-5 lines.

    {text}
    """

    return ask_llm(prompt)