from backend.database.connection import SessionLocal
from backend.model.KnowledgeChunk import KnowledgeChunk


def store_chunks(chunks, embeddings):
    """
    Store chunk text and embeddings into PostgreSQL.
    """

    db = SessionLocal()

    try:
        for chunk, embedding in zip(chunks, embeddings):

            record = KnowledgeChunk(
                content=chunk.page_content,
                embedding=embedding,
                chunk_metadata=chunk.metadata
            )

            db.add(record)

        db.commit()

        print(f"Stored {len(chunks)} chunks successfully.")

    except Exception as e:
        db.rollback()
        print("Error while storing chunks:", e)
        raise

    finally:
        db.close()