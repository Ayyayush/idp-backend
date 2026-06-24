import chromadb
from chromadb.utils import embedding_functions

sentence_transformer_ef = (
    embedding_functions.SentenceTransformerEmbeddingFunction(
        model_name="all-MiniLM-L6-v2"
    )
)

client = chromadb.PersistentClient(
    path="./chroma_db"
)

collection = client.get_or_create_collection(
    name="knowledge_base",
    embedding_function=sentence_transformer_ef
)


def add_document(text, doc_id):

    collection.upsert(
        ids=[doc_id],
        documents=[text]
    )


def search_document(query, top_k=5):

    return collection.query(
        query_texts=[query],
        n_results=top_k
    )