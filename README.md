🧠 Fast Long-Term Memory AI
(Streamlit + Ollama + FAISS)

A lightweight AI chat application with long-term memory, running fully local.

🔥 Built With

🧠 Ollama (phi model) — LLM responses

⚡ FAISS — Fast vector similarity search

🧮 Local hash-based embeddings — No external embedding API

🎨 Streamlit — Interactive UI

This project demonstrates how to build a memory-augmented AI assistant running completely offline.

🚀 Features

💬 Chat interface powered by Streamlit

🧠 Long-term memory storage

🔎 Vector similarity search using FAISS

🧮 Lightweight local embeddings (no OpenAI API)

📝 Automatic memory extraction from conversation

👁 Displays retrieved memories for transparency

📁 Project Structure

LONG_MEMORY
│
├── app.py              # Main Streamlit application
├── requirements.txt    # Python dependencies
├── .gitignore
└── venv/               Virtual environment

⚙️ Requirements

Python 3.8+

Ollama installed locally

phi model pulled in Ollama

🧩 Install Ollama

Download and install Ollama:

👉 https://ollama.com

Then pull the model:

ollama pull phi


Start Ollama:

ollama run phi


Ensure the API is running at:

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


If you don't have a requirements file yet:

pip install streamlit faiss-cpu numpy requests

3️⃣ Run the App
streamlit run app.py


Open in browser:

http://localhost:8501

🧠 How Memory Works
🔹 Memory Creation

When a user sends a message:

The LLM checks if it contains long-term information

If yes, it returns a short summary labeled:

MEMORY:


That summary is embedded and stored in FAISS

🔹 Memory Retrieval

Before generating a reply:

The system searches similar past memories

Injects relevant memories into the prompt

The assistant responds with contextual awareness

🛠️ Technical Overview
🧮 Embeddings

Uses deterministic hash-based embedding:

np.random.seed(abs(hash(text)) % (2**32))
np.random.rand(384)


This approach is:

⚡ Fast

🏠 Fully local

🪶 Lightweight

⚠️ Not semantically strong (demo purpose)

🔎 Vector Search

FAISS IndexFlatL2

Top-K retrieval (default: 3)

🧩 Prompt Structure

The assistant is forced to respond in this format:

MEMORY:
REPLY:


This enables:

Clean parsing

Automatic memory storage

Clear reasoning vs response separation

🧪 Example Use Case

User:

I am training for a marathon in October.

Stored Memory:

User is training for a marathon in October.

Later...

User:

How should I structure my week?

The assistant automatically recalls marathon training context.

🔧 Customization
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

Ollama Embeddings API

Add persistent storage (SQLite / JSON)

Add memory deletion/editing

Add conversation export

Deploy on cloud

📜 License

Open-source project — free to use and modify.
