import json
import os
import math

class MemoryStore:
    def __init__(self):
        
        self.file_path = "simple_memory.json"
        self.memories = []
        self._load_from_disk()

    def add_memory(self, text: str, metadata: dict, vector: list):
        """Save a memory to the list and file."""
        memory_item = {
            "content": text,
            "metadata": metadata,
            "vector": vector
        }
        self.memories.append(memory_item)
        self._save_to_disk()

    def search_memories(self, query_vector: list, limit: int = 3):
        """Find relevant memories using Math (Cosine Similarity)."""
        if not self.memories:
            return []

        scored_memories = []
        for mem in self.memories:
            score = self._cosine_similarity(query_vector, mem["vector"])
            scored_memories.append({
                "content": mem["content"],
                "metadata": mem["metadata"],
                "score": score
            })

        scored_memories.sort(key=lambda x: x["score"], reverse=True)
        return scored_memories[:limit]

    def get_all_memories(self):
        """Return all memories for the UI sidebar."""
        return [
            {**m["metadata"], "content": m["content"]} 
            for m in self.memories
        ]

    def _cosine_similarity(self, v1, v2):
        """Manual math to compare two vectors (No NumPy needed)."""
        dot_product = sum(a * b for a, b in zip(v1, v2))
        magnitude_v1 = math.sqrt(sum(a * a for a in v1))
        magnitude_v2 = math.sqrt(sum(a * a for a in v2))
        if magnitude_v1 * magnitude_v2 == 0:
            return 0
        return dot_product / (magnitude_v1 * magnitude_v2)

    def _save_to_disk(self):
        with open(self.file_path, "w") as f:
            json.dump(self.memories, f)

    def _load_from_disk(self):
        if os.path.exists(self.file_path):
            try:
                with open(self.file_path, "r") as f:
                    self.memories = json.load(f)
            except:
                self.memories = []