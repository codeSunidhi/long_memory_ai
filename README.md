🧠 Fast Long-Term Memory AI (Streamlit + Ollama + FAISS)

A lightweight AI chat application with long-term memory, built using:

🧠 Ollama (phi model) for LLM responses

⚡ FAISS for fast vector similarity search

🧮 Simple local hash-based embeddings (no external embedding API)

🎨 Streamlit for the UI

This project demonstrates how to build a memory-augmented AI assistant running fully local.

🚀 Features

Chat interface powered by Streamlit

Long-term memory storage

Vector similarity search using FAISS

Lightweight local embeddings (no OpenAI API required)

Automatic memory extraction from conversation

Displays retrieved memories for transparency

📁 Project Structure
LONG_MEMORY/
│
├── venv/                # Virtual environment
├── app.py               # Main Streamlit application
├── requirements.txt     # Python dependencies
├── .gitignore
└── pyvenv.cfg

⚙️ Requirements

Python 3.8+

Ollama installed locally

phi model pulled in Ollama

🧩 Install Ollama

Download and install Ollama:

👉 https://ollama.com

Then pull the phi model:

ollama pull phi


Start Ollama server (if not already running):

ollama run phi


Or ensure the API is running at:

http://localhost:11434

🐍 Setup Instructions
1️⃣ Create Virtual Environment (Optional)
python -m venv venv


Activate it:

Windows

venv\Scripts\activate


Mac/Linux

source venv/bin/activate

2️⃣ Install Dependencies
pip install -r requirements.txt


If you don't have a requirements file yet, use:

streamlit
faiss-cpu
numpy
requests

3️⃣ Run the App
streamlit run app.py


Open in browser:

http://localhost:8501

🧠 How Memory Works
1. Memory Creation

When a user sends a message:

The LLM determines whether it contains important long-term information

If yes, it returns a short summary labeled as:

MEMORY: <summary>


That summary gets embedded and stored in FAISS

2. Memory Retrieval

Before generating a reply:

The system searches similar past memories

Injects relevant memories into the prompt

The assistant responds with contextual awareness

🛠️ Technical Overview
Embeddings

Uses a simple deterministic hash-based embedding:

np.random.seed(abs(hash(text)) % (2**32))
np.random.rand(384)


This is:

Fast

Fully local

Lightweight

Not semantically strong (demo purpose)

Vector Search

FAISS IndexFlatL2

Top-K retrieval (default: 3)

Prompt Structure

The assistant is forced to respond in this format:

MEMORY: <summary or NONE>

REPLY:
<assistant reply>


This allows:

Clean parsing

Automatic memory storage

Clear separation of reasoning vs response

🧪 Example Use Case

User:

I am training for a marathon in October.


Stored Memory:

User is training for a marathon in October.


Later:

How should I structure my week?


The assistant will recall marathon training context automatically.

🔧 Customization

You can modify:

Variable	Purpose
OLLAMA_MODEL	Change to another Ollama model
EMBED_DIM	Change embedding vector size
TOP_K	Number of memories retrieved
⚠️ Limitations

Embeddings are random hash-based (not semantic)

Memory resets when Streamlit session restarts

No persistent storage (RAM only)

Requires local Ollama server

💡 Future Improvements

Replace simple embeddings with:

SentenceTransformers

Ollama embeddings API

Add persistent storage (SQLite / JSON)

Add memory deletion/editing

Add conversation export

Deploy on cloud

📜 License

Open-source project — free to use and modify.