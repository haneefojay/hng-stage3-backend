# 🧠 DocuLens AI — Developer Documentation Assistant

DocuLens AI is an intelligent documentation assistant built for **HNG Stage 3**.  
It helps developers quickly understand coding concepts, frameworks, and libraries — right from **Telex.im**.  

Instead of manually searching docs, DocuLens uses an **LLM-powered engine** to generate accurate, concise explanations of programming topics.

---

## 🚀 Features

✅ **Instant Answers** — Ask questions like *“What is useState in React?”* or *“How do I connect PostgreSQL in Laravel?”*  
✅ **LLM-Powered Intelligence** — Powered by **Groq Llama 3.1**, fine-tuned for developer content  
✅ **Multi-Ecosystem Coverage** — Supports documentation across 10+ major developer ecosystems:
- Python (FastAPI, Django, Flask, etc.)
- JavaScript (React, Next.js, Node.js)
- TypeScript
- Go
- Java
- C#
- PHP (Laravel)
- Rust  
✅ **Memory-Aware Context** — Keeps short-term memory per user/channel  
✅ **Automatic Summaries** — Summarizes long documentation into 2 short, clear sentences  
✅ **Error-Resilient** — Graceful fallbacks and consistent JSON responses  
✅ **Telex.im Integration** — Responds directly to users in Telex workspaces

---

## 🏗️ Architecture


---

## ⚙️ Tech Stack

- **FastAPI** – RESTful API framework  
- **Groq API (Llama 3.1)** – for intelligent doc explanations  
- **Python 3.12+**  
- **httpx + asyncio** – for async requests  
- **BeautifulSoup4** – (optional legacy fallback)  
- **Telex A2A Protocol** – for agent communication  

---

## 📡 API Endpoints

### `POST /webhook`
Telex.im calls this route whenever a user sends a message.

**Request Body:**
```json
{
  "message": "Explain useState in React."
}
```

**Response:**
{
  "response_type": "message",
  "text": "📘 **DocuLens AI Response:**\n\nThe `useState` hook in React manages component state, allowing updates based on user actions. It returns a state variable and a function to update it."
}

## 🛠️ Setup & Local Development

### Clone the Repository
```bash
git clone https://github.com/yourusername/hng-stage3-backend.git
cd hng-stage3-backend
```

### Create a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # (Mac/Linux)
venv\Scripts\activate     # (Windows)
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Create a .env File
```bash
GROQ_API_KEY=your_groq_api_key
```

### Run the Server
```bash
uvicorn app.main:app --reload
```

### Test Locally
```bash
curl -X POST http://127.0.0.1:8000/query -H "Content-Type: application/json" -d '{"message": "Explain useState in React"}'
```

## 🏁 Credits

Built by Haneef Ojutalayo
Backend Developer | AI Engineer