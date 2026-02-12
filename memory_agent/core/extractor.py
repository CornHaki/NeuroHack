import json
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from core.llm import get_llm  

class Extractor:
    def __init__(self):
        self.llm = get_llm()
        
        self.prompt = PromptTemplate(
            template="""
            Analyze the user's message.
            Extract any FACT, PREFERENCE, CONSTRAINT, or INSTRUCTION that should be remembered long-term.
            
            Rules:
            1. If casual (e.g. "Hello"), return null.
            2. If important, extract it.
            
            Format as JSON:
            {{
                "should_remember": true,
                "fact": "User's budget is $50",
                "category": "constraint"
            }}
            
            Or: {{ "should_remember": false }}
            
            User Message: {input}
            """,
            input_variables=["input"]
        )

    def extract(self, text: str):
        chain = self.prompt | self.llm | JsonOutputParser()
        try:
            return chain.invoke({"input": text})
        except Exception as e:
            print(f"Extraction Error: {e}")
            return {"should_remember": False}