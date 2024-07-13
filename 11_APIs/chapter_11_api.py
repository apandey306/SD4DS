from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from chapter_11_functions import fit_trendline, country_trendline

app = FastAPI()


@app.get("/say_hi/")
def say_hi():
    return {"Hi": "There"}


# You could also consider adding type annotations to this function
# Using type annotations here has a number of benefits. 
# You can use a type checking tool to avoid common errors and validate your input data. 
@app.get("/say_hello/{name}")
def say_hello(name):
    return {"Hello": name}

