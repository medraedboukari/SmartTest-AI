
import chromadb


def search_products(query, n_results=3):

    # Connect to persistent ChromaDB
    client = chromadb.PersistentClient(
        path="rag/chroma_db"
    )

    collection = client.get_collection(
        name="fakestore_products"
    )

    # Semantic search
    results = collection.query(
        query_texts=[query],
        n_results=n_results
    )

    print("\nSearch query:", query)
    print("\nRetrieved documents:")

    for i, document in enumerate(results["documents"][0]):

        metadata = results["metadatas"][0][i]
        distance = results["distances"][0][i]

        print("\n-----------------------------")
        print("Product:", metadata["title"])
        print("Category:", metadata["category"])
        print("Price:", metadata["price"], "USD")
        print("Distance:", round(distance, 4))
        print("Description:", document)


if __name__ == "__main__":

    query = input("Enter your search query: ")

    search_products(query)
