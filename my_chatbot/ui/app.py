import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import tempfile
import streamlit as st
from core.chat import start_chat, send_message
from tools.retriever import load_document

# all formats Docling supports
SUPPORTED_FORMATS = [
    "pdf",
    "docx",
    "pptx",
    "xlsx",
    "csv",
    "html",
    "md",
    "png",
    "jpg",
    "jpeg",
    "tiff",
]

st.set_page_config(page_title="SKRs_AI Chatbot", page_icon="🤖")
st.title("🤖 AI Chatbot")

with st.sidebar:
    st.header("Load Document")

    # file upload
    uploaded_file = st.file_uploader("Upload a document", type=SUPPORTED_FORMATS)

    if uploaded_file:
        # extract correct extension so Docling detects format
        ext = os.path.splitext(uploaded_file.name)[1]

        with tempfile.NamedTemporaryFile(delete=False, suffix=ext) as tmp:
            tmp.write(uploaded_file.read())
            tmp_path = tmp.name

        with st.spinner(f"Indexing {uploaded_file.name}..."):
            load_document(tmp_path)

        st.success(f"✅ {uploaded_file.name} indexed!")

    # URL input
    st.divider()
    url_input = st.text_input("Or paste a URL")
    if st.button("Load URL"):
        if url_input:
            with st.spinner("Fetching and indexing..."):
                load_document(url_input)
            st.success("✅ URL indexed!")

# initialize messages
if "messages" not in st.session_state:
    st.session_state.messages = start_chat()

# display conversation history
for message in st.session_state.messages:
    if message["role"] == "system":
        continue
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# input box
user_input = st.chat_input("Type your message...")

if user_input:
    with st.chat_message("user"):
        st.markdown(user_input)
    reply = send_message(st.session_state.messages, user_input)
    with st.chat_message("assistant"):
        st.markdown(reply)
