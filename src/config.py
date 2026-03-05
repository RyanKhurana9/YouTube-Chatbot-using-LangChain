import os
from dotenv import load_dotenv

load_dotenv()

GOOGLE_API_KEY   = os.getenv("GOOGLE_API_KEY", "")
EMBEDDING_MODEL  = "models/gemini-embedding-001"
LLM_MODEL        = "gemini-2.5-flash-lite"
LLM_TEMPERATURE  = 0.4

CHUNK_SIZE       = 3000
CHUNK_OVERLAP    = 500

RETRIEVER_K      = 5
