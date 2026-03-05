from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.vectorstores import VectorStoreRetriever

import config


def build_vector_store(transcript: str) -> FAISS:
    """
    Split a transcript into chunks and index them in a FAISS vector store.

    Args:
        transcript: Full transcript text.

    Returns:
        A populated FAISS vector store.
    """
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=config.CHUNK_SIZE,
        chunk_overlap=config.CHUNK_OVERLAP,
    )
    chunks = splitter.create_documents([transcript])

    embedding = GoogleGenerativeAIEmbeddings(model=config.EMBEDDING_MODEL)
    return FAISS.from_documents(documents=chunks, embedding=embedding)


def get_retriever(vector_store: FAISS) -> VectorStoreRetriever:
    """
    Wrap a FAISS vector store in a similarity-search retriever.

    Args:
        vector_store: A populated FAISS index.

    Returns:
        A LangChain retriever that returns the top-k most similar chunks.
    """
    return vector_store.as_retriever(
        search_type="similarity",
        search_kwargs={"k": config.RETRIEVER_K},
    )
