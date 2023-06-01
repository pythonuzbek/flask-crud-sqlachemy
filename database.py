from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('postgresql://postgres:1@localhost/flask')
Session = sessionmaker(bind=engine)
session = Session()
