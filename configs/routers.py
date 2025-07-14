from fastapi import APIRouter

from apps.employees.routes import employee_v1_router

main_router = APIRouter()
main_router.include_router(employee_v1_router, prefix="/v1/employee", tags=['employee'])
