from datetime import datetime

from sqlalchemy import create_engine, Column, String, Integer, DateTime
from sqlalchemy.orm import DeclarativeBase, sessionmaker


class Base(DeclarativeBase):
    pass


engine = create_engine(
    'sqlite:///url_shortener.db',
    pool_size=10,
    max_overflow=20,
    pool_recycle=3600
)
Session = sessionmaker(bind=engine, expire_on_commit=False)


class ShortURL(Base):
    __tablename__ = 'short_urls'
    id = Column(Integer, primary_key=True)
    original_url = Column(String(500))
    short_key = Column(String(10), unique=True)
    created_at = Column(DateTime, default=datetime.now)
    visits = Column(Integer, default=0)


Base.metadata.create_all(engine)
