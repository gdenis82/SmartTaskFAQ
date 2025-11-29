from app.db.session import engine
from sqlalchemy import text


async def test_db_connection():
    async with engine.connect() as conn:
        result = await conn.execute(text("SELECT 1"))
        assert result.scalar() == 1