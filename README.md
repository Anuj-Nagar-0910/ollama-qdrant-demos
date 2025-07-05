# 🧠 Ollama + Qdrant Demos

This repo showcases a working example of how to use **local LLMs with vector search** using [Ollama](https://ollama.com) and [Qdrant](https://qdrant.tech).

---

## 🚀 Features

- Embed and store documents using `SentenceTransformer`
- Search using Qdrant’s vector engine
- Simple integration via `docker-compose`
- Use Ollama for local LLM context and generation

---

## 📦 How to Run

### 1. Start services
```bash
docker-compose up -d
```

### 2. Ingest documents
```bash
python app/ingest.py
```

### 3. Run query search
```bash
python app/query.py
```

---

## 💡 Notes

- Qdrant runs locally at `localhost:6333`
- Ollama is preconfigured to use `llama2` (update `ollama_config.json` as needed)
- Customize `ingest.py` to include your own docs or PDFs

---

## 📬 Contact

Made with 🔥 by Anuj – prompt engineer in progress!
