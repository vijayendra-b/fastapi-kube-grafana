import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base
url=f"postgresql://{os.getenv('DB_USER','postgres')}:{os.getenv('DB_PASSWORD','postgres')}@{os.getenv('DB_HOST','localhost')}:{os.getenv('DB_PORT','5432')}/{os.getenv('DB_NAME','inventorydb')}"
engine=create_engine(url,pool_pre_ping=True)
SessionLocal=sessionmaker(bind=engine)
Base=declarative_base()
