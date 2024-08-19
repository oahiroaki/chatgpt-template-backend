from fastapi import FastAPI

from models import ChatCompletionParamter
from services import chat_completions

app = FastAPI()

@app.get("/")
def read_root():
    return {"msg": "Hello World"}

@app.post("/chat/completions")
def post_chat_completions(parameter: ChatCompletionParamter):
    return chat_completions(parameter)