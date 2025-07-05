import qdrant_client
from sentence_transformers import SentenceTransformer

# Connect to Qdrant
client = qdrant_client.QdrantClient(":memory:")

# Load embedding model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Query input
query_text = "How can I run LLMs locally?"

# Generate query embedding
query_vector = model.encode(query_text).tolist()

# Search in Qdrant
hits = client.search(collection_name="ai_knowledge", query_vector=query_vector, limit=3)

print("Top results:")
for hit in hits:
    print(f"- {hit.payload['text']} (score={hit.score:.4f})")