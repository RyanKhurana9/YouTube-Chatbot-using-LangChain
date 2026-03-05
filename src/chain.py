from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableParallel, RunnablePassthrough, RunnableLambda
from langchain_core.output_parsers import StrOutputParser
from langchain_core.vectorstores import VectorStoreRetriever

import config

PROMPT_TEMPLATE = """
You are a helpful assistant.
Answer ONLY from the provided transcript context.
If the context is insufficient, just say you don't know.

Context:
{context}

Question: {question}
"""


def _format_docs(retrieved_docs) -> str:
    return "\n\n".join(doc.page_content for doc in retrieved_docs)


def build_chain(retriever: VectorStoreRetriever):
    """
    Assemble the full RAG chain:
        retriever → prompt → LLM → string output

    Args:
        retriever: A LangChain retriever backed by the FAISS index.

    Returns:
        A runnable chain that accepts a question string and returns an answer.
    """
    llm = ChatGoogleGenerativeAI(
        model=config.LLM_MODEL,
        temperature=config.LLM_TEMPERATURE,
    )

    prompt = PromptTemplate(
        template=PROMPT_TEMPLATE,
        input_variables=["context", "question"],
    )

    parallel_chain = RunnableParallel({
        "context":  retriever | RunnableLambda(_format_docs),
        "question": RunnablePassthrough(),
    })

    return parallel_chain | prompt | llm | StrOutputParser()
