import os
from dotenv import load_dotenv

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

load_dotenv(os.path.join(os.path.dirname(__file__), 'env/.env.development'))

engine = create_engine(os.environ.get("DB_CONNECTION_STRING"))
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()


def init_db():
    import app.models
    from app.models.Shop import Shop
    Base.metadata.create_all(bind=engine)

    db_session.add(
        Shop(name="test_shop", imageUrl="example_url")
    )
    db_session.commit()
