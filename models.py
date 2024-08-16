
from typing import Any, List, Literal
from pydantic import BaseModel


class ChatMessage(BaseModel):
    """チャットメッセージ
    """

    content: str
    """Required

    The contents of the system message.
    """

    role: str
    """Required

    The role of the messages author.
    """

    name: str | None = None
    """Optional

    An optional name for the participant.    
    Provides the model information to differentiate between participants of the same role.
    """


class ChatCompletionParamter(BaseModel):
    """
    チャット補完APIパラメータ
    """

    messages: List[ChatMessage]
    """Required

    A list of messages comprising the conversation so far.
    """

    model: str
    """Required

    ID of the model to use.
    See the model endpoint compatibility table for details on which models work with the Chat API.
    """

    frequency_penalty: float | None = None

    logit_bias: Any

    logprobs: bool | None = False
    """Optional

    Whether to return log probabilities of the output tokens or not.
    If true, returns the log probabilities of each output token returned in the content of message.
    """

    top_logprobs: int | None = None
    """
    An integer between 0 and 20 specifying the number of most likely tokens to return at each token position, each with an associated log probability.
    logprobs must be set to true if this parameter is used.
    """

    max_tokens: int | None = None
    """
    The maximum number of tokens that can be generated in the chat completion.
    The total length of input tokens and generated tokens is limited by the model's context length.
    """

    n: int | None = 1
    """
    How many chat completion choices to generate for each input message.
    Note that you will be charged based on the number of generated tokens across all of the choices. Keep n as 1 to minimize costs.
    """

    presence_penalty: float | None = 0
    """
    Number between -2.0 and 2.0.
    Positive values penalize new tokens based on whether they appear in the text so far, increasing the model's likelihood to talk about new topics.
    """
