from sqlalchemy import Column, Integer, Text, DateTime, func
from sqlalchemy.dialects.postgresql import JSONB
from pgvector.sqlalchemy import Vector

from database.connection import Base


class KnowledgeChunk(Base):
    __tablename__ = "knowledge_chunks_webside"

    id = Column(Integer, primary_key=True, index=True)

    content = Column(Text, nullable=False)

    embedding = Column(Vector(768), nullable=False)

    chunk_metadata = Column(
        "metadata",
        JSONB,
        nullable=True
    )

    created_at = Column(
        DateTime,
        server_default=func.current_timestamp()
    )