import os
from fastapi import FastAPI
from dotenv import load_dotenv
from pydantic import BaseModel

from .models import ChatCompletionParamter

from .services import chat_completions


app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/chat/completions")
def post_chat_completions(parameter: ChatCompletionParamter):
    return chat_completions(parameter)