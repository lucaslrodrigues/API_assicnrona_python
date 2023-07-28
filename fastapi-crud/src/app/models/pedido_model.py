import os
from sqlalchemy.sql import func
from databases import Database

from sqlalchemy import (
    colum,
    DateTime,
    Integer,
    MetaData,
    String,
    Table,
    create_engine
)
DATABASE_URL = "postgresql://postgres:postgres@db:5433/learning"
# DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL)
metadata = MetaData()

notes = Table(
    "notes",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("title", String(50)),
    Column("description", String(50)),
    Column("created_date", DateTime, default=func.now(), nullable=False),
)

database = Database(DATABASE_URL)