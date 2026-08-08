from backend.rag.embedding import embedding_chunks
from backend.rag.vector_store import store_chunks


def upload_document(document_path):
    chunks, embeddings = embedding_chunks(document_path)

    print(f"Chunks Generated: {len(chunks)}")
    print(f"Embeddings Generated: {len(embeddings)}")

    store_chunks(
        chunks=chunks,
        embeddings=embeddings
    )

    print("Data stored successfully.")