import chromadb
from chromadb.utils import embedding_functions

class MemoryStore:
    def __init__(self):
        self.client = chromadb.Client()
        ef = embedding_functions.DefaultEmbeddingFunction()
        self.collection = self.client.get_or_create_collection("research", embedding_function=ef)

    def upsert(self, facts: list[dict]):
        for i, fact in enumerate(facts):
            self.collection.upsert(
                documents=[fact["text"]],
                metadatas=[{"source": fact.get("source",""), "confidence": fact.get("confidence", 0.8)}],
                ids=[f"fact_{self.collection.count()}_{i}"]
            )

    def query(self, goal: str, n=5):
        results = self.collection.query(query_texts=[goal], n_results=min(n, max(self.collection.count(),1)))
        return results["documents"][0] if results["documents"] else []

    def query_all(self, goals: list[str]):
        all_chunks = []
        for goal in goals:
            all_chunks.extend(self.query(goal))
        return list(set(all_chunks))

    def covered_goals(self, goals: list[str]):
        covered = []
        for goal in goals:
            results = self.query(goal, n=1)
            if results:
                covered.append(goal)
        return covered
