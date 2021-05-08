from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
import cloudinary

cloudinary.config(
    cloud_name= "postgresql-asymmetrical-64288",
    api_key= "data-key",
    api_secret ="dfgdfhdfhfghfghfghfghfghfgh"
)

# SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
SQLALCHEMY_DATABASE_URL = "postgres://vztbtnsawpretu:5e5f7e92555c0bf3bd914bb5598ef3a020631a3b6832e5f65c2d8337075a2635@ec2-3-234-85-177.compute-1.amazonaws.com:5432/de2v2355mcq1je"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
