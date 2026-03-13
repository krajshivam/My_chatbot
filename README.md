# AI Chatbot

A conversational AI chatbot built with Groq (Llama 3.3) and Streamlit. Ask anything — it remembers the full conversation context.

🔗 **Live Demo**: [https://py-mychatbotdeployable.streamlit.app/]

---

## Features

- Multi-turn conversation with memory
- Powered by Llama 3.3 70B via Groq API
- Clean web UI built with Streamlit
- Formatted responses with numbered points
- Fast inference — Groq runs Llama at 500+ tokens/second

---

## Tech Stack

| Layer | Technology |
|---|---|
| AI Model | Llama 3.3 70B (via Groq) |
| UI | Streamlit |
| Language | Python 3.14 |
| Package Manager | UV |
| Deployment | Streamlit Cloud |

---

## Project Structure

```
ai-chatbot-deploy/
├── config/
│   └── settings.py       # Centralized config — model, temperature, tokens
├── core/
│   └── chat.py           # Chat logic — API calls, conversation memory
├── ui/
│   └── app.py            # Streamlit web interface
├── main.py               # Terminal version
├── requirements.txt      # Dependencies
└── .env                  # API keys (never committed)
```

---

## Run Locally

**1. Clone the repo:**
``` bash
git clone https://github.com/krajshivam/ai-chatbot-deploy.git
cd ai-chatbot-deploy
```

**2. Install dependencies:**
```bash
pip install -r requirements.txt
```

**3. Add your API key:**

Create a `.env` file in the root:
```
GROQ_API_KEY=your-groq-api-key-here
```

Get a free API key at [console.groq.com](https://console.groq.com)

**4. Run:**
```bash
streamlit run ui/app.py
```

Open [http://localhost:8501](http://localhost:8501) in your browser.

---

## How It Works


User types message
        ↓
Message added to conversation history
        ↓
Full history sent to Groq API (Llama 3.3)
        ↓
AI reply added to history
        ↓
Response displayed in chat UI


The conversation history is maintained in `st.session_state` — this gives the AI memory across turns without any database.

---

## Full Version (with RAG)

This is the lightweight deployment version. The full version includes:

- PDF, DOCX, PPTX, URL document loading via Docling
- Vector search using ChromaDB
- RAG pipeline — answers questions from uploaded documents

Full version repo: [github.com/krajshivam/My_chatbot](https://github.com/krajshivam/My_chatbot)

---

## Environment Variables

| Variable | Description |
|---|---|
| `GROQ_API_KEY` | Your Groq API key |

---

## License

MIT

