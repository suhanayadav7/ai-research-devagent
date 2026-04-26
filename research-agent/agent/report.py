from groq import Groq
import os
from dotenv import load_dotenv
load_dotenv()

class ReportEngine:
    def __init__(self):
        self.client = Groq(api_key=os.environ["GROQ_API_KEY"])

    def build(self, chunks: list[str], target: str) -> str:
        context = "\n".join(chunks[:30])
        prompt = f"""You are a research analyst. Using the facts below, write a structured report about {target}.

Include these sections:
# {target} — Research Report
## Executive Summary
## Background & Early Life
## Career & Key Achievements
## Philosophy & Worldview
## Recent News & Activity
## Notable Quotes

Facts gathered:
{context}

Write a detailed, well-structured report."""
        resp = self.client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role":"user","content":prompt}],
            temperature=0.3,
            max_tokens=2000
        )
        return resp.choices[0].message.content
