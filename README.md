---
title: Boxbnb
emoji: 📦
colorFrom: yellow
colorTo: red
sdk: gradio
sdk_version: 6.30.0
app_file: app.py
pinned: false
---

# Boxbnb: Agent-Powered Business Assistant

EECE 798S, C3: Introduction to Agents.

Boxbnb is a (fictional) short-stay rental platform for cats: boxes, sunbeams, keyboards, laundry piles.
Customer support is handled by **Bob the dog**, a golden retriever who was hired by mistake.
He answers questions from the company documents, takes bookings from cats, and logs complaints from humans.

## What's in it

- **Business knowledge:** `me/business_summary.txt` and `me/about_business.pdf`, both loaded into the system prompt.
- **Persona and instructions:** kept as two separate blocks; the instructions win if they conflict.
- **Router:** a separate LLM call that labels each message by intent (`general` / `lead` / `feedback`),
  speaker (cat / human / unknown), and tone. It picks the tools and instructions Bob gets for that turn,
  with a keyword fallback if the call fails.
- **Tools** (defined MCP style, with manual function calling):
  - `record_customer_interest(email, name, message)` logs a booking to `logs/leads.jsonl`.
  - `record_feedback(question)` logs complaints and unanswered questions to `logs/feedback.jsonl`.
- **Memory:** the chat history plus a per-chat profile (name, email, cat or human).
- **Bonus, reflection:** each draft is checked against a checklist before it's sent. If problems are found,
  Bob rewrites it, and the result is logged to `logs/reflections.jsonl` and shown in the chat.
- **Bonus, deployment:** live at https://huggingface.co/spaces/lauremhsn/boxbnb (`app.py`).

`business_agent.ipynb` builds everything step by step with outputs. `app.py` is the same agent as a standalone app.

## Run it locally

In PowerShell, from the repo folder:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
copy .env.example .env   # then paste your Gemini key into .env
python app.py
```

Then open http://127.0.0.1:7860.

## On Hugging Face Spaces

The key is stored as a Space secret named `GOOGLE_API_KEY`, never committed.
Logs written by the Space are temporary and reset when it restarts.
