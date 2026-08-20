import os
from google import genai

from rag.chunker import chunking


EMBEDDING_MODEL = "gemini-embedding-2"

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def get_embedding(text):
    response = client.models.embed_content(
        model=EMBEDDING_MODEL,
        contents=text
    )

    return response.embeddings[0].values


def embedding_chunks(document_path):
    chunks = chunking(document_path)
    embeddings = []

    for chunk in chunks:
        embedding = get_embedding(chunk.page_content)
        embeddings.append(embedding)

    return chunks, embeddings