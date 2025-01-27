import uuid

from db import ShortURL


def create_short_url(original_url: str) -> str:
    """Create a shortened URL entry in DB and return short key."""
    from db import Session
    with Session() as session, session.begin():
        while True:
            short_key = uuid.uuid4().hex[:6]
            if not session.query(ShortURL).filter_by(short_key=short_key).first():
                break
        session.add(ShortURL(original_url=original_url, short_key=short_key))
        return short_key


def get_host_url():
    """Adjust to your domain or keep localhost for local usage."""
    return "http://localhost:8080"
