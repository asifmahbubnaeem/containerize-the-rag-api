import chromadb

client = chromadb.PersistentClient(path="./db")
collection = client.get_or_create_collection("docs")

with open("cucumber.txt", "r") as f:
    text = f.read()

collection.add(documents=[text], ids=["cucumber"])

print("Embedding stored in Chroma")
