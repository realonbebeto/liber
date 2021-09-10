from starlette.routing import Host
import uvicorn
import os
from fastapi import FastAPI
from dtos import Employee, Department
from entities import Employee as EntityEmployee
from entities import Department as EntityDepartment
from fastapi_sqlalchemy import DBSessionMiddleware, db
from dotenv import load_dotenv

load_dotenv(".env")

app = FastAPI()
app.add_middleware(DBSessionMiddleware, db_url = os.environ["DATABASE_URL"])

@app.get("/")
async def root():
    return {'message': "Hello World"}

@app.post("/add-employee", response_model=Employee)
async def add_employee(employee: Employee):
    db_emp = EntityEmployee(fname = employee.fname, mname= employee.mname, lname=employee.lname, email=employee.email, department_id=employee.department_id)
    db.session.add(db_emp)
    db.session.commit()
    return db_emp

@app.get("/employees/")
async def get_employees():
    employees = db.session.query(EntityEmployee).all()
    return employees

@app.post("/add-department", response_model=Department)
async def add_department(department: Department):
    db_dprt = EntityDepartment(name = department.name)
    db.session.add(db_dprt)
    db.session.commit()
    return db_dprt

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)