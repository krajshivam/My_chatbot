from docling.document_converter import DocumentConverter
from tools.embedder import index_chunks, search_chunks

_collection = None


def load_document(source: str):
    global _collection

    converter = DocumentConverter()
    result = converter.convert(source)

    markdown = result.document.export_to_markdown()

    # split into sentences/lines first
    lines = markdown.split("\n")

    chunks = []
    current_chunk = ""

    for line in lines:
        current_chunk += " " + line

        # only create a chunk when it has enough content
        if len(current_chunk) >= 500:
            chunks.append(current_chunk.strip())
            current_chunk = ""

    # add remaining content
    if current_chunk.strip():
        chunks.append(current_chunk.strip())

    _collection = index_chunks(chunks)
    print(f"Indexed {len(chunks)} chunks")


def retrieve(query: str, top_k: int = 5) -> str:
    """Returns relevant context for a query."""

    if _collection is None:
        return ""

    chunks = search_chunks(query, _collection, top_k)
    return "\n\n".join(chunks)
