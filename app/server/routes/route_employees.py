from typing import List

from fastapi import APIRouter
from fastapi import HTTPException
from fastapi import status
from server.db.models.employees import Employees
from server.db.repository.employees import retreive_employees


router = APIRouter()


@router.get("/{company_name}", response_description="Список сотрудников компании")
async def get_employees(company_name: str) -> List[Employees]:
    employees_list = await retreive_employees(company_name)
    if not employees_list:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Список сотрудников для компании {company_name} не найден",
        )
    return employees_list
