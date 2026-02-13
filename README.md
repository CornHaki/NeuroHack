# 🧠 NeuroMemory: Infinite Context for AI Agents
### *The Cure for LLM Amnesia. Real-time, Long-term Memory for 1,000+ Turn Conversations.*

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python)
![Streamlit](https://img.shields.io/badge/Frontend-Streamlit-red?style=for-the-badge&logo=streamlit)
![LangChain](https://img.shields.io/badge/Orchestration-LangChain-green?style=for-the-badge&logo=langchain)
![Groq](https://img.shields.io/badge/AI_Engine-Groq_Llama3-orange?style=for-the-badge&logo=nvidia)

---

## 🚨 The Problem: "The Goldfish Effect"
Modern LLMs have a fatal flaw: **Context Windows**.
* **They Forget:** As a conversation grows (100+ turns), early facts are pushed out.
* **They are Slow:** Feeding 50,000 tokens of history into a model for every query creates massive latency.
* **They are Expensive:** Re-processing the same history costs money with every API call.

**The Challenge:** How do you make an AI remember a user's name mentioned in Turn 1 while answering a question in Turn 1,000—without crashing the system?

---

## 💡 The Solution: NeuroMemory Architecture
**NeuroMemory** is an intelligent memory layer that sits *between* the user and the LLM. It acts as a hippocampal index for AI, decoupling "processing" (LLM) from "storage" (Vector Database).

Instead of forcing the LLM to read the entire chat history, our system:
1.  **Extracts** key facts automatically in the background.
2.  **Embeds** them into a lightweight vector store.
3.  **Retrieves** only the *precise* memories relevant to the current query.
4.  **Injects** context dynamically at runtime.

### 🚀 Key Features
* **⚡ Zero-Latency Retrieval:** Uses local embeddings (`all-MiniLM-L6-v2`) and optimized cosine similarity to fetch memories in <200ms.
* **📚 Infinite Context:** effectively scales to 1,000, 10,000, or 1M+ turns without increasing LLM prompt size.
* **🧠 Self-Updating:** The AI decides *what* is worth remembering (facts/preferences) vs. what is noise (chitchat).
* **🛡️ Hackathon-Optimized:** Includes a "Time Travel" simulation script to instantly generate and prove 1,000-turn recall capabilities.

---

## 🛠️ Tech Stack

| Component | Technology | Why we chose it |
| :--- | :--- | :--- |
| **LLM Engine** | **Groq (Llama-3.3-70B)** | Blazing fast inference (300+ tokens/s) for real-time feel. |
| **Orchestration** | **LangChain** | Robust framework for chaining extraction and retrieval. |
| **Embeddings** | **HuggingFace (MiniLM)** | Local, privacy-first, and free vector generation. |
| **Frontend** | **Streamlit** | Interactive, clean UI for live demos. |
| **Memory Store** | **JSON / Vector Hybrid** | Custom lightweight implementation for portability and speed. |

---

## 📸 How It Works (Architecture)

```mermaid
graph TD
    A[User Query: 'What is my secret code?'] --> B(Embedding Engine)
    B --> C{Vector Search}
    C -->|Query Vector| D[(Memory Store - 1000 Items)]
    D -->|Top 3 Matches| E[Context Injection]
    E --> F[LLM Prompt]
    F --> G[Groq / Llama 3]
    G --> H[Response: 'Your code is BlueMonkey99']
    E --> F[LLM Prompt]
    F --> G[Groq / Llama 3]
    G --> H[Response: "Your code is BlueMonkey99"]
