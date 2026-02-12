import json
import random
import sys
import os


sys.path.append(os.path.dirname(os.path.abspath(__file__)))


from langchain_community.embeddings import HuggingFaceEmbeddings
from datetime import datetime

print("⏳ Loading Embedding Model (This ensures the memory is actually findable)...")

embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")


secret_text = "My secret code is 'BlueMonkey99'."
print(f"🔹 Embedding the needle: '{secret_text}'")
real_vector = embeddings.embed_query(secret_text)

needle = {
    "content": secret_text,
    "metadata": {
        "turn": 1,
        "category": "security",
        "timestamp": str(datetime.now())
    },
    "vector": real_vector 
}


print("🔹 Generating 999 distractor memories...")
haystack = []
for i in range(2, 1001):
    item = {
        "content": f"I talked about topic {i} on turn {i}. Just chitchat.",
        "metadata": {
            "turn": i,
            "category": "chitchat",
            "timestamp": str(datetime.now())
        },
        "vector": [random.random() for _ in range(384)] 
    }
    haystack.append(item)


full_memory = [needle] + haystack
with open("memory_agent/simple_memory.json", "w") as f:
    json.dump(full_memory, f)

print(f"✅ SUCCESSFULLY INJECTED {len(full_memory)} MEMORIES.")
print("The 'Needle' now has a real vector matching your query.")