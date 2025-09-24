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
```

### Frontend (Electron desktop)
_Open a new terminal/window:_
```powershell
cd frontend\electron
npm install
npm start
```

### 🧱 Project Structure
```
offline-business-ai-assistant/
├─ backend/
│  ├─ app.py                 # FastAPI local API (chat stub + examples)
│  ├─ requirements.txt
│  └─ data/sample/invoices.csv
└─ frontend/
   └─ electron/
      ├─ package.json
      ├─ main.js
      ├─ preload.js          # points UI to http://127.0.0.1:8000
      └─ renderer.html       # simple chat UI
```

### 🗺️ Roadmap & Milestones
- **Phase 1 – Requirements & Architecture (10%)**
  Model choice, offline constraints, data flows, UX and security plan.
- **Phase 2 – Security & Infra (20%)**
  App lock, local auth (PIN/YubiKey/Biometrics), encrypted storage (SQLCipher),
  secrets handling, audit logs; packaging (PyInstaller/electron-builder).
- **Phase 3 – Conversational AI (30%)**
  Local LLM via llama.cpp or Ollama; prompt templates; offline STT/TTS
  (whisper.cpp / Piper).
- **Phase 4 – Business Logic & Integrations (20%)**
  Workflows (CRM/reporting), adapters to local systems, RBAC.
- **Phase 5 – Testing & Delivery (20%)**
  Functional, security, and offline performance tests; docs; signed installers.
```

```
## 🔐 Security Notes
- 100% offline: no external network calls.
- Encrypt sensitive data (recommend **SQLCipher**) and store secrets via OS keychain.
- Local user auth + **RBAC**; session lock/timeout.
- Tamper-evident audit logs (hash chain) and offline/signed updates.
- Principle of least privilege for all local adapters/integrations.
```

```
## 📸 Screenshots
<p align="center">
  <img src="docs/screenshot-1.png" width="600" alt="Desktop UI – chat view" />
</p>

> Add PNGs to `docs/` and reference them as above.
```

```
## 📄 License
This project is licensed under the **MIT License** – see [LICENSE](./LICENSE).
```

``` 
## 🙋 Author
**Allen Aryeetey** — Senior Network & Security Engineer | AI Enthusiast  
Reach out on Upwork for collaboration on offline AI, security, and integrations.




