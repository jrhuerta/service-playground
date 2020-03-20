from alaya.clients import models
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

conn = create_engine("mysql://root:root@127.0.0.1/patient_service", echo=True)
Session = sessionmaker(bind=conn)

session = Session()
