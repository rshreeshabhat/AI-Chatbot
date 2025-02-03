import streamlit as st
import ollama
import random

MODEL_NAME = "deepseek-r1:8b"

# Custom CSS for futuristic styling
st.markdown(
    """
    <style>
        body {
            background-color: #0d0d0d;
            color: #00FFFF;
        }
        .stChatMessage {
            background: rgba(0, 255, 255, 0.1);
            border-radius: 12px;
            padding: 5px;
            margin-bottom: 10px;
            box-shadow: 0 0 10px #00FFFF;
        }
        .stChatMessage:hover {
            box-shadow: 0 0 20px #00FFFF;
        }
        .stTitle {
            text-align: center;
            font-size: 2em;
            font-weight: bold;
            text-shadow: 0px 0px 10px #00FFFF;
        }
        @keyframes glitch {
            0% { text-shadow: 2px 2px 0px #FF00FF; }
            33% { text-shadow: -2px -2px 0px #00FFFF; }
            66% { text-shadow: 2px 2px 0px #ffff00 ; }
            100% { text-shadow: -2px -2px 0px #ff00FF; }
        }
        .glitch {
            animation: glitch 1s infinite alternate;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown('<h1 class="stTitle glitch">Deepseek R1:8b Chat Bot</h1>', unsafe_allow_html=True)


if "messages" not in st.session_state:
    st.session_state["messages"] = []

for message in st.session_state["messages"]:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


user_input = st.chat_input("What's on your mind today? 🤔")

if user_input:
    st.chat_message("user").markdown(user_input)
    st.session_state["messages"].append({"role": "user", "content": user_input})

    response = ollama.chat(model=MODEL_NAME, messages=st.session_state["messages"]) ["message"]["content"].strip()
    response = response.replace("<think>", "").replace("</think>", "").strip()

    with st.chat_message("assistant"):
        st.markdown(response)
    st.session_state["messages"].append({"role": "assistant", "content": response})