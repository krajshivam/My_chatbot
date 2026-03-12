import chromadb

chroma_client = chromadb.Client()


def index_chunks(chunks: list[str], collection_name: str = "documents"):
    """Stores chunks in ChromaDB. Embeddings handled automatically."""

    collection = chroma_client.get_or_create_collection(collection_name)

    ids = []
    for i in range(len(chunks)):
        ids.append(f"chunk_{i}")

    collection.add(documents=chunks, ids=ids)  # ← moved outside loop

    return collection


def search_chunks(query: str, collection, top_k: int = 3) -> list[str]:
    """Finds most relevant chunks for a query."""

    results = collection.query(query_texts=[query], n_results=top_k)

    return results["documents"][0]
