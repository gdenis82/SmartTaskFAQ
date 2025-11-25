from sqlalchemy import Column, Integer, String, Text, DateTime, func
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class QueryLog(Base):
    __tablename__ = 'query_logs'

    id = Column(Integer, primary_key=True, index=True)
    question = Column(Text, nullable=False)
    answer = Column(Text, nullable=False)
    sources = Column(String, nullable=True)
    input_tokens = Column(Integer)
    output_tokens = Column(Integer)
    response_time_ms = Column(Integer)