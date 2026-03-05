 🎬 YouTube RAG Chatbot

> Ask questions about any YouTube video and get accurate, context-aware answers — powered by LangChain and Retrieval-Augmented Generation (RAG).

---

## 📌 Overview

**YouTube RAG Chatbot** is a conversational AI pipeline that lets you have a natural conversation with any YouTube video. Paste a video ID, ask your questions, and get answers grounded directly in the video's transcript — no hallucinations, no guesswork.

Built with **LangChain**, **FAISS**, and **Google Gemini**, this project is a clean, modular, end-to-end RAG system broken into focused Python modules.

---

## ✨ Features

- 🎙️ **Transcript Extraction** — Fetches captions from any YouTube video via the YouTube Transcript API
- ✂️ **Smart Chunking** — Splits long transcripts into overlapping chunks to preserve context at boundaries
- 🧠 **Semantic Search** — Embeds chunks into FAISS for fast, meaning-aware retrieval
- 💬 **Interactive Q&A Loop** — Ask follow-up questions in a continuous terminal session
- 🔌 **Modular Design** — Each concern lives in its own file; swap models or vector stores with one-line changes
- ⚡ **Efficient RAG Pipeline** — Only the most relevant chunks are passed to the LLM, keeping costs low and accuracy high

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| RAG Orchestration | [LangChain](https://langchain.com) |
| Transcript Fetching | [YouTube Transcript API](https://pypi.org/project/youtube-transcript-api/) |
| Vector Store | [FAISS](https://faiss.ai/) |
| Embeddings | Google Gemini `gemini-embedding-001` |
| LLM | Google Gemini `gemini-2.5-flash-lite` |
| Language | Python 3.12 |

---

## 🏗️ Project Structure

```
youtube_rag/
│
├── config.py           # All settings: models, chunk size, retriever k, etc.
├── transcript.py       # Fetches and returns the YouTube transcript
├── vector_store.py     # Chunking, embedding → FAISS index + retriever factory
├── chain.py            # RAG prompt template + LangChain pipeline assembly
├── main.py             # Entry point — interactive Q&A loop
│
├── requirements.txt
├── .env.example
└── README.md
```

### Module responsibilities at a glance

| File | Responsibility |
|---|---|
| `config.py` | Single source of truth for all tunable parameters |
| `transcript.py` | `fetch_transcript(video_id)` → raw transcript string |
| `vector_store.py` | `build_vector_store(transcript)` + `get_retriever(store)` |
| `chain.py` | `build_chain(retriever)` → end-to-end runnable |
| `main.py` | Wires everything together; runs the Q&A loop |

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-username/youtube-rag-chatbot.git
cd youtube-rag-chatbot
```

### 2. Create a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate        # macOS / Linux
venv\Scripts\activate           # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set your API key

Copy `.env.example` to `.env` and fill in your key:

```bash
cp .env.example .env
```

```env
GOOGLE_API_KEY=your_google_api_key_here
```

### 5. Run the chatbot

```bash
python main.py
```

---

## 💬 Example Session

```
Fetching transcript for video: Gfr50f6ZBvo
Transcript length: 84,302 characters

Building vector store...
Vector store ready.

YouTube RAG Chatbot ready! Type 'exit' to quit.

You: Is nuclear fusion discussed in this video?# LANGCHAIN
