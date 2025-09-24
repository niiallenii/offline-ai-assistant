
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import os, csv

app = FastAPI(title="Offline AI Assistant - Local API")
DATA_PATH = os.path.join(os.path.dirname(__file__), "data", "sample", "invoices.csv")

class ChatRequest(BaseModel):
    message: str
    top_k: int = 3

class ChatResponse(BaseModel):
    answer: str
    refs: list

def load_invoices():
    rows = []
    with open(DATA_PATH, newline='') as f:
        reader = csv.DictReader(f)
        rows = list(reader)
    return rows

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/chat", response_model=ChatResponse)
def chat(req: ChatRequest):
    rows = load_invoices()
    msg = req.message.lower()
    refs = []
    answer = ""

    paid = [r for r in rows if r["paid"].lower() == "true"]
    unpaid = [r for r in rows if r["paid"].lower() == "false"]

    def sum_total(items): 
        return sum(float(r["total"]) for r in items) if items else 0.0

    if "unpaid" in msg or "not paid" in msg or "arrears" in msg:
        refs = unpaid[:req.top_k]
        answer = ("All invoices are paid."
                  if not unpaid else
                  f"There are {len(unpaid)} unpaid invoices totaling ${sum_total(unpaid):.2f}. "
                  f"Example: {unpaid[0]['invoice_id']} ({unpaid[0]['customer']}, ${unpaid[0]['total']}).")
    elif "paid" in msg:
        refs = paid[:req.top_k]
        answer = ("No paid invoices found."
                  if not paid else
                  f"There are {len(paid)} paid invoices totaling ${sum_total(paid):.2f}. "
                  f"Latest paid: {sorted(paid, key=lambda r: r['date'], reverse=True)[0]['invoice_id']}.")
    elif "latest" in msg or "recent" in msg:
        latest = sorted(rows, key=lambda r: r["date"], reverse=True)[:req.top_k]
        refs = latest
        answer = "Most recent invoices: " + ", ".join(r["invoice_id"] for r in latest)
    elif "total" in msg:
        answer = (f"Grand total: ${sum_total(rows):.2f} | "
                  f"Paid: ${sum_total(paid):.2f} | Unpaid: ${sum_total(unpaid):.2f}")
        refs = rows[:req.top_k]
    else:
        refs = rows[:req.top_k]
        answer = ("Offline assistant stub. Try: "
                  "'show unpaid invoices', 'show paid invoices', 'latest invoices', 'totals'.")

    return ChatResponse(answer=answer, refs=refs)

