# 🤖 AI Chatbot with RAG Pipeline

A conversational AI chatbot that answers questions from your documents. Upload a PDF, Word doc, PowerPoint, or paste a URL — then ask anything about it.

Built with Groq (Llama 3.3), Docling, ChromaDB, and Streamlit.

---

## Features

- Multi-turn conversation with persistent memory
- RAG pipeline — answers questions from uploaded documents
- Supports PDF, DOCX, PPTX, XLSX, CSV, HTML, Markdown, images and more
- URL loading — paste any webpage and ask questions about it
- Semantic search using ChromaDB vector database
- Powered by Llama 3.3 70B via Groq API (free tier available)
- Clean web UI built with Streamlit

---

## Tech Stack

| Layer | Technology |
|---|---|
| AI Model | Llama 3.3 70B (via Groq) |
| Document Parsing | Docling (IBM) |
| Vector Database | ChromaDB |
| Embeddings | all-MiniLM-L6-v2 (via ChromaDB) |
| UI | Streamlit |
| Language | Python 3.14 |
| Package Manager | UV |

---

## Project Structure

```
my_chatbot/
├── config/
│   └── settings.py       # Centralized config — model, temperature, tokens
├── core/
│   └── chat.py           # Chat logic — conversation memory + RAG injection
├── tools/
│   ├── embedder.py       # ChromaDB — store and search vectors
│   └── retriever.py      # Docling document loading + chunking pipeline
├── ui/
│   └── app.py            # Streamlit web interface with document upload
├── main.py               # Terminal version
├── requirements.txt      # Dependencies
└── .env                  # API keys (never committed)
```

---

## How RAG Works

```
INDEXING (once per document):
Document (PDF/URL/DOCX)
        ↓
Docling parses and exports to markdown
        ↓
Split into 500 character chunks
        ↓
ChromaDB converts chunks to vectors (embeddings)
        ↓
Vectors + original text stored in ChromaDB

RETRIEVAL (every query):
User question
        ↓
ChromaDB converts question to vector
        ↓
Finds top 5 most similar chunk vectors (cosine similarity)
        ↓
Returns original text of those chunks

GENERATION:
Retrieved chunks + user question
        ↓
Injected into prompt as context
        ↓
Llama 3.3 generates answer using that context
        ↓
Final answer displayed
```

---

## Run Locally

**1. Clone the repo:**
```bash
git clone https://github.com/krajshivam/My_chatbot.git
cd My_chatbot
```

**2. Install UV (if not installed):**
```bash
pip install uv
```

**3. Install dependencies:**
```bash
uv add groq streamlit python-dotenv docling chromadb
```

**4. Add your API key:**

Create a `.env` file in the root:
```
GROQ_API_KEY=your-groq-api-key-here
```

Get a free API key at [console.groq.com](https://console.groq.com)

**5. Run:**
```bash
uv run streamlit run ui/app.py
```

Open [http://localhost:8501](http://localhost:8501) in your browser.

> **Note:** First run downloads Docling's ML models (~500MB) and ChromaDB's embedding model (~80MB). This is a one-time download — subsequent runs are fast.

---

## Usage

1. Upload a document from the sidebar (PDF, DOCX, PPTX etc.) or paste a URL
2. Wait for indexing to complete
3. Ask any question about the document in the chat

**Example questions after uploading a company policy PDF:**
- "What is the refund policy for hardware?"
- "How many paid leaves do employees get per year?"
- "What encryption standard is used for data storage?"

---

## Key Technical Decisions

**Why Docling over pypdf:**
Docling understands document structure — tables, headings, columns — not just raw text extraction. This significantly improves chunk quality.

**Why minimum chunk size (500 chars) over splitting by blank lines:**
Splitting by blank lines separated headings from their content, causing retrieval to return headings without actual information. Minimum size chunking keeps related content together.

**Why cosine similarity over euclidean distance:**
Cosine similarity measures semantic direction not vector magnitude — two sentences with the same meaning but different lengths are correctly identified as similar.

**Why top_k=5:**
Tested with 3 — some answers were incomplete. 5 retrieves enough context without adding noise that confuses the AI.

---

## Limitations

| Limitation | Production Fix |
|---|---|
| ChromaDB in-memory — resets on restart | Use persistent ChromaDB or Pinecone |
| Heavy dependencies — not free-tier deployable | Deploy on Railway/Render paid tier |
| Query sensitive — wording affects retrieval | Add query rewriting or hybrid search |
| No streaming — full response at once | Use Groq streaming API |
| No authentication | Add Streamlit-Authenticator |

---

## Lightweight Deployed Version

A lightweight version without RAG is live on Streamlit Cloud:

🔗 [https://py-mychatbotdeployable.streamlit.app/] | [Deploy Repo](https://github.com/krajshivam/My_chatbot_deployable.git)
---

## License

MIT
