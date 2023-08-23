from fastapi import FastAPI, Request
from starlette.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from solution import get_random_500

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get("/healthcheck/")
async def healthcheck():
    return {"message": "Everything OK!"}

class SchRandomFloats(BaseModel):
    inp_str: str = Field(examples=["This is an example sentence"])

@app.post("/random_floats/")
async def random_floats(x: SchRandomFloats):
    return {"output": get_random_500()}
