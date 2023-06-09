from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

import json


app = FastAPI()

class Person(BaseModel):
    id: Optional[int] = None
name: str
age: int
gender: str



with open('people.json', 'r') as f:
    people = json.load(f)['people']


    print(people)



    @app.get('/person/{p_id}')
    def get_person(p_id: int):
        person = [p for p in people if p['id'] == p_id]
        return person[0] if len(person) > 0 else {}



# @app.get('/')
# async def hello():
#     return {'example': 'this is an example', 'data':0}


# @app.get('/something')
# def something():
#     return {'Data': 'something'}