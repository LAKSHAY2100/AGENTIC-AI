from typing import Annotated,Literal
from typing_extensions import TypedDict
from langchain_core.messages import AnyMessage
from langgraph.graph.message import add_messages

class State(TypedDict):
    messages : Annotated[list[AnyMessage],add_messages]