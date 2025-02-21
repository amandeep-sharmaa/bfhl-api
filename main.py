from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import re

app = FastAPI()

USER_ID = "john_doe_17091999"
EMAIL = "john@xyz.com"
ROLL_NUMBER = "ABCD123"

class DataInput(BaseModel):
    data: List[str]

@app.get("/bfhl")
def get_operation_code():
    return {"operation_code": 1}

@app.post("/bfhl")
def process_data(input_data: DataInput):
    try:
        numbers = [item for item in input_data.data if item.isdigit()]
        alphabets = [item for item in input_data.data if re.match(r'^[a-zA-Z]$', item)]
        highest_alphabet = [max(alphabets, key=lambda x: x.upper())] if alphabets else []
        
        response = {
            "is_success": True,
            "user_id": USER_ID,
            "email": EMAIL,
            "roll_number": ROLL_NUMBER,
            "numbers": numbers,
            "alphabets": alphabets,
            "highest_alphabet": highest_alphabet
        }
        return response

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
