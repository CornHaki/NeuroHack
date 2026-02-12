from langchain_community.embeddings import HuggingFaceEmbeddings
import os

class Retriever:
    def __init__(self):

        print("Loading local embedding model... (this happens only once)")
        self.embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

    def embed_text(self, text: str):
        return self.embeddings.embed_query(text)