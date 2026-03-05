from transcript import fetch_transcript
from vector_store import build_vector_store, get_retriever
from chain import build_chain


def main():
    video_id = "Gfr50f6ZBvo"

    # ── Step 1: Fetch transcript ──────────────────────────────────────────
    print(f"Fetching transcript for video: {video_id}")
    transcript = fetch_transcript(video_id)
    print(f"Transcript length: {len(transcript)} characters\n")

    # ── Step 2: Index into vector store ──────────────────────────────────
    print("Building vector store...")
    vector_store = build_vector_store(transcript)
    retriever    = get_retriever(vector_store)
    print("Vector store ready.\n")

    # ── Step 3: Build RAG chain ───────────────────────────────────────────
    chain = build_chain(retriever)

    # ── Step 4: Interactive Q&A loop ──────────────────────────────────────
    print("YouTube RAG Chatbot ready! Type 'exit' to quit.\n")
    while True:
        question = input("You: ").strip()
        if question.lower() in ("exit", "quit"):
            break
        if not question:
            continue

        answer = chain.invoke(question)
        print(f"\nAssistant: {answer}\n")


if __name__ == "__main__":
    main()
