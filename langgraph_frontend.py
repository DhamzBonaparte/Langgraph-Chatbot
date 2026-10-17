import streamlit as st
from langhgraph_backend import chatbot, retrieveAllThreads
from langchain_core.messages import HumanMessage
import uuid


# UTILITY FUNCTIONS
def generateThreadID():
    return uuid.uuid4()


def reset_chat():
    thread_id = generateThreadID()
    st.session_state["thread_id"] = thread_id
    add_thread(st.session_state["thread_id"])
    st.session_state["message_history"] = []


def add_thread(thread_id):
    if thread_id not in st.session_state["chat_threads"]:
        st.session_state["chat_threads"].append(thread_id)


def load_convo(thread_id):
    state = chatbot.get_state(config={"configurable": {"thread_id": thread_id}})
    return state.values.get("messages", [])


# SESSION SETUP

if "message_history" not in st.session_state:
    st.session_state["message_history"] = []

if "thread_id" not in st.session_state:
    st.session_state["thread_id"] = generateThreadID()

if "chat_threads" not in st.session_state:
    st.session_state["chat_threads"] = retrieveAllThreads()

add_thread(st.session_state["thread_id"])
# SIDEBAR

st.sidebar.title("Langgraph Chatbot")

if st.sidebar.button("New chat"):
    reset_chat()

st.sidebar.header("My Conversations")

for thread_id in st.session_state["chat_threads"][::-1]:
    if st.sidebar.button(thread_id):
        st.session_state["thread_id"] = thread_id
        messages = load_convo(thread_id)
        temp = []
        for message in messages:
            if isinstance(message, HumanMessage):
                role = "user"
                temp.append({"role": role, "content": message.content})
            else:
                role = "assistant"
                temp.append({"role": role, "content": message.content[0]["text"]})
        st.session_state["message_history"] = temp

# CHAT
CONFIG = {"configurable": {"thread_id": st.session_state["thread_id"]}}

for message in st.session_state["message_history"]:
    with st.chat_message(message["role"]):
        st.text(message["content"])


user_input = st.chat_input("Type here")

if user_input:

    # first add the message to message_history
    st.session_state["message_history"].append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.text(user_input)

    response = chatbot.invoke(
        {"messages": [HumanMessage(content=user_input)]}, config=CONFIG
    )

    ai_message = response["messages"][-1].content
    # first add the message to message_history
    st.session_state["message_history"].append(
        {"role": "assistant", "content": ai_message[0]["text"]}
    )
    with st.chat_message("assistant"):
        st.text(ai_message[0]["text"])
