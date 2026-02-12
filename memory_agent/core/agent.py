import time
from datetime import datetime
from core.llm import get_llm  
from core.memory import MemoryStore
from core.extractor import Extractor
from core.retriever import Retriever

class MemoryAgent:
    def __init__(self):
        self.llm = get_llm()
        self.memory_store = MemoryStore()
        self.extractor = Extractor()
        self.retriever = Retriever()
        self.turn_count = 1000 

    def process_message(self, user_message: str):
        self.turn_count += 1
        
        query_vector = self.retriever.embed_text(user_message)
        relevant_memories = self.memory_store.search_memories(query_vector)
        
        memory_text = ""
        if relevant_memories:
            memory_text = "\n".join([f"- {m['content']} (Turn {m['metadata']['turn']})" for m in relevant_memories])

        system_prompt = f"""
        You are a Memory Assistant. Current Turn: {self.turn_count}.
        
        RETRIEVED HISTORY:
        {memory_text if memory_text else "No relevant history."}
        
        User: {user_message}
        Assistant:
        """
        

        response = self.llm.invoke(system_prompt)


        extraction = self.extractor.extract(user_message)
        if extraction.get("should_remember"):
            self.memory_store.add_memory(
                text=extraction['fact'],
                metadata={
                    "turn": self.turn_count,
                    "category": extraction.get("category"),
                    "timestamp": str(datetime.now())
                },
                vector=query_vector 
            )

        return {
            "response": response.content,
            "active_memories": relevant_memories,
            "new_memory_saved": extraction.get("fact") if extraction.get("should_remember") else None
        }