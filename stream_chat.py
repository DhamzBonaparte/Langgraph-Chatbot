import streamlit as st
from backend import chatbot
from langchain_core.messages import HumanMessage

st.title("Welcome to my Chatbot!")
st.subheader("Wanna talk? Have fun!")

CONFIG = {"configurable": {"thread_id": "thread-1"}}

if "message_history" not in st.session_state:
    st.session_state["message_history"] = []

for message in st.session_state["message_history"]:
    with st.chat_message(message["role"]):
        st.text(message["content"])


user_input = st.chat_input("Type here")
ai_message=None

if user_input:

    st.session_state["message_history"].append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.text(user_input)

    try:
        with st.chat_message("assistant"):
            ai_message = st.write_stream(
                message_chunk.content[0]["text"]
                for message_chunk, metadata in chatbot.stream(
                    {"messages": [HumanMessage(content=user_input)]},
                    config={"configurable": {"thread_id": "thread-1"}},
                    stream_mode="messages",
                )
            )
            st.session_state["message_history"].append(
                                            {"role": "assistant", "content": ai_message}
                                        )
    except Exception :
        st.write(" ")
  
       
