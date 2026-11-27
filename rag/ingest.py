
import requests
import chromadb

# Fake Store API
API_URL = "https://fakestoreapi.com/products"


def fetch_products():
    """Retrieve products from Fake Store API."""
    print("Connecting to Fake Store API...")

    response = requests.get(API_URL, timeout=20)
    response.raise_for_status()

    products = response.json()

    return products


def prepare_documents(products):
    """Convert products into documents for RAG indexing."""

    documents = []
    ids = []
    metadatas = []

    for product in products:

        document = f"""
Product: {product['title']}
Category: {product['category']}
Description: {product['description']}
Price: {product['price']} USD
"""

        documents.append(document.strip())
        ids.append(str(product["id"]))

        metadatas.append({
            "title": product["title"],
            "category": product["category"],
            "price": product["price"]
        })

    return documents, ids, metadatas


def index_documents(documents, ids, metadatas):
    """Store documents in a persistent ChromaDB collection."""

    print("\nConnecting to ChromaDB...")

    client = chromadb.PersistentClient(
        path="rag/chroma_db"
    )

    collection = client.get_or_create_collection(
        name="fakestore_products"
    )

    collection.upsert(
        ids=ids,
        documents=documents,
        metadatas=metadatas
    )

    return collection


if __name__ == "__main__":

    # 1. Retrieve products
    products = fetch_products()

    print(f"Products retrieved: {len(products)}")

    # 2. Prepare RAG documents
    documents, ids, metadatas = prepare_documents(products)

    print(f"Documents prepared: {len(documents)}")

    # 3. Display first document
    print("\nFirst document:")
    print(documents[0])

    # 4. Index documents in ChromaDB
    collection = index_documents(
        documents,
        ids,
        metadatas
    )

    # 5. Display indexing results
    print("\nIndexing completed!")
    print("Collection name:", collection.name)
    print("Documents stored in ChromaDB:", collection.count())
