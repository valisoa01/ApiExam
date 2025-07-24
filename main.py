from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/hello")
async def root():
    return {"message": "Hello World"}

@app.get("/welcome/{name}")
async def say_hello(name: str):
    return {"message": f"Welcome {name}"}

class Student(BaseModel):
    reference: str
    name: str
    age: int
    first_name: str

users_db: list[Student] = []

@app.post("/students")
async def create_student(student: Student):
    users_db.append(student)
    return {"message": f"Added {student.reference}"}

@app.get("/students")
async def get_students():
    return users_db

@app.put("/students/{reference}")
async def update_student(reference: str, student: Student):
    for i, user in enumerate(users_db):
        if user.reference == reference:
            users_db[i] = student
            return {"message": f"Updated student with reference {reference}"}
    return {"error": "Student not found"}
