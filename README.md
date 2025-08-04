# 📄 Information Retrieval System using Generative AI (Google Gemini + LangChain)

This is a conversational AI system that allows users to upload one or more PDF documents and interact with them using natural language queries. It combines traditional information retrieval with modern generative AI (LLMs), enabling context-aware answers from document content.

---

## 🚀 Features

- 📚 Upload and process multiple PDF documents
- 🔍 Chunk and embed document text using Google Generative AI Embeddings
- 📦 Store and retrieve embeddings using FAISS (vector store)
- 🤖 Generate accurate and conversational answers using Google Gemini (via LangChain)
- 🧠 Maintains conversation history across questions
- 🖥️ Interactive UI using Streamlit

---

## 📸 Demo Preview



---

## 🧠 Tech Stack

| Layer          | Technology Used                        |
|----------------|----------------------------------------|
| UI             | Streamlit                              |
| Backend Logic  | Python                                 |
| LLM            | Google Gemini 1.5 Pro                  |
| Embeddings     | GoogleGenerativeAIEmbeddings           |
| Vector DB      | FAISS (via LangChain)                  |
| PDF Processing | PyPDF2                                 |
| Chat Memory    | LangChain ConversationBufferMemory     |
| Environment    | dotenv (.env file for API keys)        |

---

## 🛠️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/AftabSahil/Information-Retrival-System.git
cd Information-Retrival-System
