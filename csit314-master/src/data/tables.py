from sqlalchemy import Integer, Column, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class TestCase(Base):
    __tablename__ = "TestCase"

    uuid = Column(String, primary_key=True)
    test_input = Column(String)
    test_output = Column(String)
    state = Column(int)
