# Offline Business AI Assistant (Starter)

**Offline-first** AI assistant starter you can share with clients.

- Desktop UI: Electron (renderer.html)
- Local API: FastAPI (`backend/app.py`)
- Demo data: `backend/data/sample/invoices.csv`

## Run
### Backend
```
cd backend
python -m venv .venv && source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
uvicorn app:app --reload
```
### Frontend
```
cd ../frontend/electron
npm install
npm start
```
Type: **show unpaid invoices**.

## Replace stub with real LLM + RAG
Use `llama-cpp-python` + `ChromaDB/FAISS`.
