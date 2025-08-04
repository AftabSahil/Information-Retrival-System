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
```
---
### 2. Create and activate a virtual environment

```bash
python -m venv venv
source venv/bin/activate      # for Linux/macOS
venv\Scripts\activate         # for Windows
```
---
### 3. Install dependencies
```
pip install -r requirements.txt
```
---
### 4. Configure your environment
```text
Create a .env file in the root directory and add your Google API key:
GOOGLE_API_KEY=your_google_api_key_here
```
---
### 5. Run the application
```bash
streamlit run app.py
```
---
### 🔄 System Architecture
```
graph LR
A[User Uploads PDFs] --> B[Extract Text using PyPDF2]           
B --> C[Chunk Text using LangChain Splitter]                    
C --> D[Embed Chunks using Google Generative AI Embeddings]     
D --> E[Store Embeddings in FAISS]                              
F[User Asks a Question] --> G[Search Similar Chunks from FAISS] 
G --> H[Generate Answer using Google Gemini LLM]                
H --> I[Show Answer in Streamlit Chat]                          
```
---
### 🧪 Example Use Case
Upload a set of research papers, legal documents, or policy files

Ask: "What does the document say about climate policy?"

_Get a context-aware, conversational response from the LLM, referencing document content_
---

### 🧩 Folder Structure
```bash
├── app.py                         # Main Streamlit app
├── src/
│   └── helper.py                 # PDF processing, embeddings, chain setup
├── requirements.txt              # Dependencies
├── .env                          # API key config (not included in repo)
├── setup.py                      # Optional for packaging
├── genAI project.drawio          # Architecture diagram (editable)
└── README.md                     # You're here :)
```
---
### 📌 Future Enhancements
```
 Add page-level reference for answers

 Cache vector store to avoid recomputation

 Enable multi-user session support

 Integrate file storage (e.g., S3 or local DB)

 Summarize PDFs using Gemini before chat
 ```
---
### 💡 Inspiration & Learning
```
This project gave me hands-on experience with:

Embedding-based retrieval systems

Vector databases (FAISS)

Using large language models (LLMs) for RAG (retrieval-augmented generation)

LangChain ecosystem and memory modules

Building fast AI prototypes using Streamlit
```
---

