from apps.employees.models import Employee, Department, Location, Status
from pydantic import BaseModel
from typing import List, Optional


class EmployeeSchema(BaseModel):
    id: int
    firstname: str
    lastname: str
    department: Optional[Department]
    position: str
    location: Location
    status: Status


