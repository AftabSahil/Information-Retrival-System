import os
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.llms import Ollama
from langchain_community.vectorstores import FAISS
from langchain.chains import ConversationalRetrievalChain
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain.memory import ConversationBufferMemory
from langchain.embeddings import HuggingFaceEmbeddings  # New: For embedding

from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# -------------------------------
# 1. PDF Text Extraction
# -------------------------------
def get_pdf_text(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text

# -------------------------------
# 2. Text Chunking
# -------------------------------
def get_text_chunks(text):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=20)
    chunks = text_splitter.split_text(text)
    return chunks

# -------------------------------
# 3. Vector Store using HuggingFace Embeddings
# -------------------------------
def get_vector_store(text_chunks):
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    vector_store = FAISS.from_texts(text_chunks, embedding=embeddings)
    return vector_store

# -------------------------------
# 4. Conversational Chain using Ollama (Mistral)
# -------------------------------
def get_conversational_chain(vector_store):
    llm = Ollama(model="mistral")
    memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

    conversational_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=vector_store.as_retriever(),
        memory=memory
    )
    return conversational_chain
