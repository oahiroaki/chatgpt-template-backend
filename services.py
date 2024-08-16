import os
from typing import List
from dotenv import load_dotenv
from openai import OpenAI
from openai.types.chat import ChatCompletionMessageParam, ChatCompletion

from .models import ChatCompletionParamter

load_dotenv()
CHATGPT_API_KEY = os.environ["CHATGPT_API_KEY"]


def chat_completions(parameter: ChatCompletionParamter):
    client = OpenAI(
        api_key=CHATGPT_API_KEY,
        organization='org-grtytNTy4DB5VMVvVcI1XALU',
    )
    messages: List[ChatCompletionMessageParam] = []
    for message in parameter.messages:
        if message.role == "user":
            messages.append({"role": "user", "content": message.content})
        elif message.role == "system":
            messages.append({"role": "system", "content": message.content})
        elif message.role == "assistant":
            messages.append({"role": "assistant", "content": message.content})

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages
    )

    return response