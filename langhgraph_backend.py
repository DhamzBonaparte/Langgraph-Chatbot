from typing import TypedDict, Annotated
from langgraph.graph import StateGraph, START, END
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import BaseMessage
from langgraph.checkpoint.sqlite import SqliteSaver
from langchain_core.messages import HumanMessage
from langgraph.graph.message import add_messages
from dotenv import load_dotenv
import sqlite3
import os

load_dotenv()

os.environ['LANGCHAIN_PROJECT']="Sulav-Chatbot"

model = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash-lite", google_api_key=os.getenv("GEMINI_API_KEY_10")
)


class ChatState(TypedDict):
    messages: Annotated[list[BaseMessage], add_messages]


def chat_node(state: ChatState):
    messages = state["messages"]
    response = model.invoke(messages)
    return {"messages": response}


conn = sqlite3.connect(database="chatbot.db", check_same_thread=False)
checkPointer = SqliteSaver(conn)

graph = StateGraph(ChatState)

graph.add_node("chat", chat_node)

graph.add_edge(START, "chat")
graph.add_edge("chat", END)

chatbot = graph.compile(checkpointer=checkPointer)

def retrieveAllThreads():
    all_thread = set()
    for checkpoint in checkPointer.list(None):
        all_thread.add(checkpoint.config["configurable"]["thread_id"])

    return list(all_thread)
