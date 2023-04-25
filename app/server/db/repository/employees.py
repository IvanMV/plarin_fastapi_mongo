from server.db.models.employees import Employees


async def retreive_employees(company_name: str):
    employees_list = await Employees.find({"company": company_name}).to_list()
    return employees_list
