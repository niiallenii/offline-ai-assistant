# Offline Business AI Assistant (PoC)  
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](#license)
[![Python](https://img.shields.io/badge/Python-3.10%2B-blue)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.111+-teal)](https://fastapi.tiangolo.com/)
[![Electron](https://img.shields.io/badge/Electron-30+-black)](https://www.electronjs.org/)
[![Offline](https://img.shields.io/badge/Mode-100%25%20Offline-important)](#)

**Offline-first AI assistant** starter built with **Electron (desktop UI)** + **FastAPI (local API)**.  
Ships with sample business data (invoices) and a working chat flow. Designed to add **local LLM (llama.cpp / Ollama) + RAG** securely in later phases.

> Demo runs **fully offline**. LLM integration (e.g., **Qwen2.5-7B-Instruct GGUF**) is planned in **Phase 3**.

---

## ✨ Features
- Cross-platform desktop UI (Electron) calling `http://127.0.0.1` APIs
- Local API (FastAPI) with example endpoints: `/health`, `/chat`
- Sample “business logic” over local CSV invoices (paid/unpaid/latest/totals)
- Clear security hooks (app lock, secrets, audit) for Phase 2
- Ready for **offline LLM** (llama.cpp or Ollama) & **RAG** (Chroma/FAISS)

---

## 🚀 Quickstart (Windows)

### Backend (FastAPI)
```powershell
cd backend
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
uvicorn app:app --reload --host 127.0.0.1 --port 8000
