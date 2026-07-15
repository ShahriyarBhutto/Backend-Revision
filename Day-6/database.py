from sqlalchemy import create_engine
from sqlalchemy.ext.declerative import declarative
from sqlalchemy.orm import sessionlocal


DATABASE_URL = "sqlite///./invoice.db"

engine = create_engine(DATABASE_URL)