# 🧠 NeuroMemory Agent

**A Long-Term Memory System built for the NeuroHack Challenge (IITG.ai × Smallest.ai).**

This project implements an intelligent agent with persistent memory capabilities, designed to handle long-context recall without the latency or cost of massive context windows. It utilizes vector storage to retrieve specific details even after "1,000 turns" of conversation.

---

## ⚡ Quick Start (Step-by-Step Setup)

Follow these instructions to reproduce the end-to-end demo on your local machine.

### 1. Clone & Install
Clone the repository and install the required dependencies.

```bash
git clone https://github.com/CornHaki/NeuroHack.git
cd NeuroHack
pip install -r requirements.txt

```
##
### 2. Configuration `(.env)`
Create a file named `.env` in the root directory. Add your Groq API key (Required for the LLM).

```bash
# .env content
GROQ_API_KEY="gsk_your_groq_key_here"
```
##
### 3. 🧪 Run Simulation (The "1,000 Turn" Proof)

To prove the system handles long-term memory without needing hours of chatting, run this script. It instantly injects 1,000 distinct memory vectors into the database.

```bash

python memory_agent/simulate_memory.py

```
Expected Output: ✅ SUCCESSFULLY INJECTED 1000 MEMORIES.
##

### 4. Launch the Demo UI
Start the Streamlit interface to interact with the agent.

```bash

python -m streamlit run memory_agent/app/ui.py

```
---
## 🎮 How to Test the Demo (Judges Guide)
Once the UI is running in your browser, follow these steps to verify functionality:
 #### 1. Verify Scale:
- Open the **Sidebar** (left panel).
- Click **"Refresh Memory View"**.
- Confirm that **1,000 stored vectors** are listed.  
  This indicates that the simulation executed successfully.
#### 2. Ask a "Turn 1" Question:
- Type: ```"What is my secret code?"```
- **Witness Retrieval:** The agent will ignore the 999 "distractor" memories and correctly retrieve the fact injected at Turn 1 (`BlueMonkey99`).
#### 3. Test New Memories:
- Type: ```"My favorite color is neon purple."```
#### 4. Test Recall:
- Ask: ```"What should I wear to the party?"```
- **Result:** The agent will suggest neon purple items, proving it combined old context with new context.
---
## 📂 Project Structure
```plaintext
NEUROHACK/
├── memory_agent/
│   ├── app/
│   │   ├── main.py
│   │   └── ui.py
│   ├── core/
│   │   ├── __pycache__/
│   │   ├── __init__.py
│   │   ├── agent.py
│   │   ├── extractor.py
│   │   ├── llm.py
│   │   ├── memory.py
│   │   └── retriever.py
│   ├── tests/
│   │   └── test_memory.py
│   ├── requirements.txt
│   ├── run_demo.ipynb
│   ├── simple_memory.json
│   └── simulate_memory.py
├── .env
├── .gitignore
├── check_models.py
├── READM.MD
└── simple_memory.json
```
---
## 🏗️ Architecture Overview

NeuroMemory Agent follows a retrieval-augmented memory design:

1. **User input** → processed by LLM extractor
2. **Key facts** → converted to embeddings
3. Stored in vector database (persistent memory)
4. **Future queries** → semantic search retrieves relevant memories
5. **LLM** generates response using retrieved context


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