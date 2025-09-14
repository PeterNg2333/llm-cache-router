import os ## Access to Operating System functionality
import httpx ## HTTP client for making requests
from dotenv import load_dotenv ## Load environment variables from a .env file
from fastapi import FastAPI, HTTPException ## FastAPI framework for building APIs

from pydantic import BaseModel 
from typing import List, Dict, Any

import uvicorn ## ASGI server for running FastAPI applications

## Todo: Load environment variables from a .env file


## Todo: Create Pydantic models for request and response validation
## Todo: limit the models to a specific set of strings, hint: use enum for the model field
class ChatRequest(BaseModel):
    model: str
    prompt: str

app = FastAPI()

@app.get("/")
async def read_root():
    return {"Message": "Welcome to the LLM Cache Router API"}


## Todo (challenge): Implement llm calling logic here via postman
@app.post("/chat")
async def chat(request: ChatRequest):
    ## Todo: Validate model field to be one of the allowed models
    return {"response": "This is a placeholder response"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=8000, reload=True)
    ## What is host: it is the hostname to listen on, "localhost" means the server will only be accessible from the local machine
    ## What is port: it is the port number to listen on, 8000 is a common choice for development servers