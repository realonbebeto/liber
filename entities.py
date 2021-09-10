from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

Base = declarative_base()


class Employee(Base):
    __tablename__ = "employee"

    id = Column(Integer, primary_key=True, index=True)
    fname = Column(String, nullable=False)
    mname = Column(String, nullable=True)
    lname = Column(String, nullable=False)
    email = Column(String, nullable=False)
    time_created=Column(DateTime(timezone=True), server_default=func.now())
    time_updated=Column(DateTime(timezone=True), onupdate=func.now())

    department_id = Column(Integer, ForeignKey("department.id"))

    department = relationship("Department")

class Department(Base):
    __tablename__ = "department"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    time_created = Column(DateTime(timezone=True), server_default=func.now())
    time_updated = Column(DateTime(timezone=True), onupdate=func.now())