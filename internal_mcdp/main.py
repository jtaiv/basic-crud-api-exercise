import logging
import sqlalchemy as sa
from fastapi import FastAPI, Depends

app = FastAPI()


async def client():
    return sa.create_engine("sqlite:///database.sqlite")


@app.get("/")
async def root():
    return {"message": "Hello World"}


# Add a get endpoint

# Add a post endpoint with input schema and output schema
# Add the handler function here and and pydantic schema classes on new file.

# Add a delete endpoint
