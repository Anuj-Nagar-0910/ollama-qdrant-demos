import qdrant_client
from sentence_transformers import SentenceTransformer
import os

# Load Qdrant client
client = qdrant_client.QdrantClient(":memory:")  # Change to Qdrant URL if hosted

# Load embedding model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Sample documents
docs = [
    {"id": "1", "text": "Ollama enables running LLMs locally."},
    {"id": "2", "text": "Qdrant provides vector search infrastructure."},
    {"id": "3", "text": "Docker helps containerize applications for portability."}
]

# Create embeddings and upload
vectors = [model.encode(d["text"]).tolist() for d in docs]
payloads = [{"text": d["text"]} for d in docs]

client.recreate_collection(collection_name="ai_knowledge", vectors_config={"size": 384, "distance": "Cosine"})
client.upload_collection(
    collection_name="ai_knowledge",
    vectors=vectors,
    payload=payloads,
    ids=[d["id"] for d in docs]
)

print("Documents successfully embedded and stored in Qdrant.")