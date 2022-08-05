import logging
from fastapi import FastAPI, status
from .database import SessionLocal
from . import schemas, crud

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


# Add a get endpoint
@app.get("/profile")
async def profile():
    with SessionLocal() as session:
        return crud.get_profiles(session)


@app.get("/profile/{email:str}")
async def profiles(email):
    with SessionLocal() as session:
        return crud.get_profile(session, email)


# Add a post endpoint with input schema and output schema
# Add the handler function here and and pydantic schema classes on new file.
@app.post("/profile", status_code=status.HTTP_201_CREATED)
async def create_profile(payload: schemas.Profile):
    with SessionLocal() as session:
        crud.create_profile(session, payload)


# Add a delete endpoint
@app.delete("/profile/{email:str}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_profile(email):
    with SessionLocal() as session:
        crud.delete_profile(session, email)
