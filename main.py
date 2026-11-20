from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"]
)

# Define the model first
class BMI_Calculator(BaseModel):
    name: str
    age: int
    gender: str
    phone: str = ""
    weight: float
    height: float

@app.post("/Details")
def check_Details(data: BMI_Calculator):

    if data.weight <= 0 or data.height <= 0:
        return {"message": "Please enter valid weight and height."}

    bmi = data.weight / ((data.height / 100) ** 2)

    if data.weight < 35:
        message = "Please Increase your weight"
    elif data.weight > 70:
        message = "Please Reduce your weight"
    else:
        message = "You are normally weighted"

    return {
        "name": data.name,
        "age": data.age,
        "bmi": round(bmi, 2),
        "message": message
    }