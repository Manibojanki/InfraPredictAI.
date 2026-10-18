
import os

from dotenv import load_dotenv
from sqlalchemy import URL, create_engine, text
from sqlalchemy.exc import SQLAlchemyError

load_dotenv()

database_url = URL.create(
    drivername="postgresql+psycopg2",
    username=os.getenv("DB_USER", "postgres"),
    password=os.getenv("DB_PASSWORD"),
    host=os.getenv("DB_HOST", "localhost"),
    port=int(os.getenv("DB_PORT", "5432")),
    database=os.getenv("DB_NAME", "infrapredict"),
)

engine = create_engine(database_url, pool_pre_ping=True)


def check_database_connection() -> bool:
    try:
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))
        return True
    except SQLAlchemyError:
        return False