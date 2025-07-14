# models.py
from sqlalchemy import Column, Integer, String, Enum
from database import Base
from apps.employees.enums import Department, Location, Status


class Employee(Base):
    __tablename__ = "employees"
    id = Column(Integer, primary_key=True, index=True)
    firstname = Column(String, nullable=False)
    lastname = Column(String, nullable=False)
    department = Column(Enum(Department), index=True)
    position = Column(String, index=True)
    location = Column(Enum(Location), index=True)
    status = Column(Enum(Status), index=True)