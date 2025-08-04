import asyncio
import streamlit as st
from src.helper import get_pdf_text, get_text_chunks, get_vector_store, get_conversational_chain
from dotenv import load_dotenv
load_dotenv()

try:
    asyncio.get_running_loop()
except RuntimeError:
    asyncio.set_event_loop(asyncio.new_event_loop())
# import time

def user_input(user_question):
    response = st.session_state.conversation({"question": user_question})
    st.session_state.chatHistory = response['chat_history']
    for i, message in enumerate(st.session_state.chatHistory):
        if i % 2 == 0:
            st.write("User: ", message.content)
        else:
            st.write("Reply: ", message.content)

def main():
    st.set_page_config("Information Retrieval")
    st.header("Information Retrieval System")
    
    
    user_question = st.text_input("Ask a question about the uploaded documents:")
    
    if 'conversation' not in st.session_state:
        st.session_state.conversation = None
    if "chatHistory" not in st.session_state:
        st.session_state.chatHistory = None
    
    if user_question and st.session_state.conversation:
        user_input(user_question)
    
    with st.sidebar:
        st.title("Menu:")
        pdf_docs = st.file_uploader("Upload PDF Documents and click on submit and process button", accept_multiple_files=True)
        if st.button("Submit and Process"):
            with st.spinner("processing..."):
                raw_text = get_pdf_text(pdf_docs)
                text_chunks= get_text_chunks(raw_text)
                vector_store = get_vector_store(text_chunks)
                st.session_state.conversation = get_conversational_chain(vector_store)
                
                # time.sleep(2)
                
                st.success("Files processed successfully!")
                

if __name__ == "__main__":
    main()

