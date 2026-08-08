from database.connection import SessionLocal
from model.KnowledgeChunk import KnowledgeChunk
from rag.embedding import  get_embedding


def retrieve_chunks(query, top_k=5):

    session = SessionLocal()

    try:

        query_embedding =  get_embedding(query)

        results = (
            session.query(KnowledgeChunk)
            .order_by(
                KnowledgeChunk.embedding.cosine_distance(query_embedding)
            )
            .limit(top_k)
            .all()
        )
       
        return results

    finally:
        session.close()
