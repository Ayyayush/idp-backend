import chromadb

client = chromadb.PersistentClient(
    path="./chroma_db"
)

collection = client.get_or_create_collection(
    name="knowledge_base"
)


def add_document(
    text,
    doc_id
):

    collection.add(
        documents=[text],
        ids=[doc_id]
    )


def search_document(
    query,
    top_k=3
):

    result = collection.query(
        query_texts=[query],
        n_results=top_k
    )

    return result