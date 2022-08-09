import logging
from typing import List
from fastapi import FastAPI, status
from .database import SessionLocal
from . import schemas, crud

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


# Add a get endpoint
@app.get("/profile", response_model=List[schemas.Profile])
async def profile():
    """GET http://localhost:8000/profile"""
    with SessionLocal() as session:
        return crud.get_profiles(session)


@app.get("/profile/{email:str}", response_model=schemas.Profile)
async def profiles(email):
    """GET http://localhost:8000/profile/joonas.taivainen@fellowmind.fi"""
    with SessionLocal() as session:
        return crud.get_profile(session, email)


# Add a post endpoint with input schema and output schema
# Add the handler function here and and pydantic schema classes on new file.
@app.post("/profile", status_code=status.HTTP_201_CREATED)
async def create_profile(payload: schemas.Profile):
    """
    POST http://localhost:8000/profile

        {
            "email": "joonas.taivainen@fellowmind.fi",
            "name": "Joonas Taivainen",
            "contact": "+43254326542"
        }
    """
    with SessionLocal() as session:
        crud.create_profile(session, payload)


# Add a delete endpoint
@app.delete("/profile/{email:str}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_profile(email):
    """DELETE http://localhost:8000/profile/joonas.taivainen@fellowmind.fi"""
    with SessionLocal() as session:
        crud.delete_profile(session, email)
