# 🧠 Information Retrieval System using Local LLM (Ollama + Mistral) and HuggingFace Embeddings

A privacy-preserving, conversational AI system that allows users to upload multiple PDF documents and ask context-aware questions based on their content. It leverages **local LLMs (via Ollama)** and **HuggingFace sentence embeddings**, making it ideal for offline or sensitive environments.

---

## 🚀 Features

- 📁 Upload & process multiple PDF documents
- ✂️ Chunk and embed documents using "all-MiniLM-L6-v2" from HuggingFace
- 🔎 Store chunks in a FAISS vector store
- 🤖 Interact with documents using **Mistral LLM via Ollama**
- 🧠 Maintains conversation history for multi-turn QA
- ⚙️ Fully local & offline-capable — no external API calls
- 🖥️ Simple UI built using Streamlit

---

## 🧱 Tech Stack

| Component            | Technology                         |
|---------------------|-------------------------------------|
| UI                  | Streamlit                           |
| LLM                 | Mistral (via Ollama)                |
| Embeddings          | all-MiniLM-L6-v2 (HuggingFace)      |
| Vector Database     | FAISS (via LangChain)               |
| PDF Parsing         | PyPDF2                              |
| Memory              | ConversationBufferMemory            |
| Environment Config  | python-dotenv (.env support)        |

---

## 🖼️ Architecture

```mermaid
graph TD
    A[User Uploads PDFs] --> B[Extract Text with PyPDF2]
    B --> C[Split Text into Chunks]
    C --> D[Embed Chunks using HuggingFace MiniLM]
    D --> E[Store Chunks in FAISS Vector Store]
    F[User Enters Question] --> G[Retrieve Relevant Chunks]
    G --> H[Answer using Ollama LLM (Mistral)]
    H --> I[Stream Answer via Streamlit UI]
```
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
### 4. Install Ollama (if not installed)
Visit: https://ollama.com/download
Then run:
```
ollama run mistral
This downloads and serves the Mistral model locally via the Ollama CLI.
```

---
### 5. Run the application
```bash
streamlit run app.py
```
---
### 💻 How It Works
```
Upload multiple PDF documents via the UI

System reads and extracts the full text

Text is chunked for better context resolution

Chunks are converted to vector embeddings and stored in FAISS

You ask questions; system retrieves relevant chunks

Mistral generates answers based on the content context

Responses are displayed in a chat-like format
```
---
### 🧪 Use Case Examples
📚 Research assistant for reading academic papers

🧾 Contract summarizer for legal documents

📊 QA assistant for company reports

📕 Notes reader for students
---
### 📂 Project Structure
```
├── app.py                      # Streamlit frontend
├── src/
│   └── helper.py              # Core logic (PDF, Embeddings, LLM)
├── requirements.txt           # Dependencies
├── .env                       # Environment variables (if needed)
└── README.md                  # You're here
```
