import os
import uuid
import faiss
import numpy as np
import streamlit as st
import requests
from datetime import datetime

# ===============================
# CONFIG
# ===============================

OLLAMA_MODEL = "phi"
OLLAMA_URL = "http://localhost:11434/api/generate"
EMBED_DIM = 384  # For simple hash embedding (lightweight)

TOP_K = 3

# ===============================
# SIMPLE EMBEDDING (FAST + LOCAL)
# ===============================

def simple_embed(text: str):
    np.random.seed(abs(hash(text)) % (2**32))
    return np.random.rand(EMBED_DIM).astype("float32")

# ===============================
# MEMORY STORE
# ===============================

class MemoryStore:

    def __init__(self, dim):
        self.index = faiss.IndexFlatL2(dim)
        self.memories = []

    def add(self, text):
        vec = simple_embed(text)
        self.index.add(np.array([vec]))
        self.memories.append(text)

    def search(self, query, k=3):
        if not self.memories:
            return []

        vec = simple_embed(query)
        D, I = self.index.search(np.array([vec]), min(k, len(self.memories)))
        return [self.memories[i] for i in I[0]]

# ===============================
# OLLAMA CALL
# ===============================

def call_ollama(prompt):
    response = requests.post(
        OLLAMA_URL,
        json={
            "model": OLLAMA_MODEL,
            "prompt": prompt,
            "stream": False
        }
    )
    return response.json()["response"]

# ===============================
# STREAMLIT UI
# ===============================

st.set_page_config(page_title="Fast Memory AI", layout="centered")
st.title("🧠 Fast Long-Term Memory AI")

if "messages" not in st.session_state:
    st.session_state.messages = []

if "memory" not in st.session_state:
    st.session_state.memory = MemoryStore(EMBED_DIM)

# Show chat
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

user_input = st.chat_input("Say something...")

if user_input:

    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.write(user_input)

    # Retrieve memory
    memories = st.session_state.memory.search(user_input, TOP_K)
    memory_block = "\n".join(f"- {m}" for m in memories)

    prompt = f"""
You are a helpful assistant with long-term memory.

Relevant past memories:
{memory_block if memory_block else "None"}

User message:
{user_input}

Instructions:
1. If this message contains important long-term info (goal, preference, personal fact),
   create a short memory summary.
2. Otherwise say MEMORY: NONE.
3. Then provide the assistant reply.

Respond exactly in this format:

MEMORY: <summary or NONE>

REPLY:
<assistant reply>
"""

    output = call_ollama(prompt)

    # Parse output
    if "MEMORY:" in output and "REPLY:" in output:
        memory_part = output.split("MEMORY:")[1].split("REPLY:")[0].strip()
        reply_part = output.split("REPLY:")[1].strip()
    else:
        memory_part = "NONE"
        reply_part = output

    # Store memory if exists
    if memory_part != "NONE" and len(memory_part) > 5:
        st.session_state.memory.add(memory_part)

    # Show reply
    st.session_state.messages.append({"role": "assistant", "content": reply_part})
    with st.chat_message("assistant"):
        st.write(reply_part)

    # Show retrieved memories
    if memories:
        with st.expander("🔎 Retrieved Memories"):
            for m in memories:
                st.write("- " + m)