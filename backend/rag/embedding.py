import ollama
from rag.chunker import chunking


EMBEDDING_MODEL = "nomic-embed-text"


def embedding_chunks(document_path):
    chunks = chunking(document_path)
    embeddings = []

    for chunk in chunks:
        response = ollama.embed(
            model=EMBEDDING_MODEL,
            input=chunk.page_content
        )

        embeddings.append(response["embeddings"][0])

    return chunks, embeddings


def get_embedding(text):
    response = ollama.embed(
        model=EMBEDDING_MODEL,
        input=text
    )

    return response["embeddings"][0]