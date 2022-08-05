from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

# Add a get endpoint

# Add a post endpoint with input schema and output schema
# Add the handler function here and and pydantic schema classes on new file.

