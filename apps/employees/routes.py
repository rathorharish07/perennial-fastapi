# main.py
from fastapi import Depends
from fastapi_limiter.depends import RateLimiter
from sqlalchemy import select, and_
from sqlalchemy.ext.asyncio import AsyncSession
from database import get_db
from apps.employees.models import Employee
from apps.employees.enums import Department, Location, Status
from apps.employees.schemas import EmployeeSchema
from typing import List, Optional

from typing import List, Union
from fastapi import APIRouter, status

employee_v1_router = APIRouter()


@employee_v1_router.get("/search", response_model=List[EmployeeSchema], dependencies=[Depends(RateLimiter(times=100, seconds=60))])
async def search_employees(
    department: Department | None = None,
    location: Location | None = None,
    status: Status | None = None,
    position: str | None = None,
    last_id: int | None = None,
    limit: int = 50,
    db: AsyncSession = Depends(get_db),
):
    filters = []
    if department: filters.append(Employee.department == department)
    if location: filters.append(Employee.location == location)
    if status: filters.append(Employee.status == status)
    if position: filters.append(Employee.position.ilike(f"%{position}%"))
    if last_id: filters.append(Employee.id > last_id)

    stmt = (
        select(Employee)
        .where(and_(*filters))
        .order_by(Employee.id)
        .limit(limit)
    )
    results = (await db.execute(stmt)).scalars().all()
    return results
