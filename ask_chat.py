from src.db import PgVectorConnection
from src.embeddings import TextEmbedder
from src.llm import LLMEngine
import time


def process_query(query, embedder, db, llm, k=60):
    print("\nProcessing query...")
    start_time = time.time()

    emb = embedder.generate_embeddings_from_string(query)
    results = db.find_similar(query, emb, k)
    context = ";".join([row[2] for row in results if row[2].strip()])
    response_stream = llm.ask(query, context)
    end_time = time.time()
    processing_time = end_time - start_time
    print(
        f"\nFound {len(results)} relevant documents in {processing_time:.2f} seconds:"
    )
    print("\n🤖 Response:")
    for chunk in response_stream:
        if chunk.choices[0].delta.content:
            print(chunk.choices[0].delta.content, end="", flush=True)
    print("\n")


def main():
    embedder = TextEmbedder()
    db = PgVectorConnection()
    llm = LLMEngine()

    print("\n🚗 Welcome to Draiver Assistant! (Type 'exit' to quit)")
    print("------------------------------------------------")

    while True:
        try:
            query = input("\n❓ Please enter your question: ").strip()
            if query.lower() in ["exit", "quit", "q"]:
                print("\n👋 Thank you for using Draiver Assistant. Goodbye!")
                break
            if not query:
                print("Please enter a valid question!")
                continue
            process_query(query, embedder, db, llm)
        except KeyboardInterrupt:
            print("\n\n👋 Program interrupted. Goodbye!")
            break
        except Exception as e:
            print(f"\n❌ Error occurred: {str(e)}")
            print("Please try again or type 'exit' to quit.")


if __name__ == "__main__":
    main()
