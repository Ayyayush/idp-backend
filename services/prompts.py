CLASSIFICATION_PROMPT = """
Classify the document.

Types:
1. Invoice
2. Resume
3. Financial Statement
4. Other

Return only type.
"""


JSON_EXTRACTION_PROMPT = """
Extract all entities.

Return only valid JSON.
"""