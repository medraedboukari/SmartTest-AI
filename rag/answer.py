
import os
import chromadb
from groq import Groq
from dotenv import load_dotenv

# ==========================================
# 1. Load environment variables
# ==========================================

load_dotenv(override=True)

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError(
        "GROQ_API_KEY not found. Check your .env file."
    )

# Initialize Groq client
groq_client = Groq(api_key=api_key)


# ==========================================
# 2. Connect to ChromaDB
# ==========================================

chroma_client = chromadb.PersistentClient(
    path="rag/chroma_db"
)

collection = chroma_client.get_collection(
    name="fakestore_products"
)


# ==========================================
# 3. Retrieve relevant documents
# ==========================================

def retrieve_context(question, n_results=3):

    results = collection.query(
        query_texts=[question],
        n_results=n_results
    )

    documents = results["documents"][0]

    if not documents:
        return ""

    context = "\n\n".join(documents)

    return context


# ==========================================
# 4. Generate answer using Groq
# ==========================================

def generate_answer(question):

    print("\nSearching ChromaDB...")

    context = retrieve_context(question)

    if not context:
        return "No relevant information found in the database."

    print("Context retrieved successfully.")

    print("\nGenerating answer with Groq...")

    response = groq_client.chat.completions.create(
        model="openai/gpt-oss-120b",

        messages=[
            {
                "role": "system",
                "content": (
                    "You are SmartTest-AI, an intelligent assistant. "
                    "Answer the user's question using only the "
                    "provided context. "
                    "Do not invent information. "
                    "If the context does not contain the answer, "
                    "explain that you do not have enough information."
                )
            },
            {
                "role": "user",
                "content": f"""
Retrieved context:

{context}

User question:

{question}

Provide a clear and helpful answer.
"""
            }
        ],

        temperature=0.2
    )

    return response.choices[0].message.content


# ==========================================
# 5. Main program
# ==========================================

if __name__ == "__main__":

    print("=" * 45)
    print("       SMARTTEST-AI - RAG SYSTEM")
    print("=" * 45)

    question = input("\nAsk your question: ")

    try:

        answer = generate_answer(question)

        print("\n" + "=" * 45)
        print("RAG GENERATED ANSWER")
        print("=" * 45)

        print(answer)

    except Exception as error:

        print("\nError:", error)
