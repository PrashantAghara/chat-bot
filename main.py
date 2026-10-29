import streamlit as st
from langchain_core.messages import HumanMessage

from agentic_bot import bot

CONFIG = {"configurable": {"thread_id": "1"}}
st.title("Agentic Chatbot")

user_input = st.chat_input("Send a message")

if user_input:
    with st.chat_message("user"):
        st.text(user_input)

    response = bot.invoke(
        {"messages": [HumanMessage(content=user_input)]}, config=CONFIG
    )

    with st.chat_message("assistant"):
        st.text(response["messages"][-1].content)
