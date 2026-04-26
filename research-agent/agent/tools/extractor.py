from groq import Groq
import os, json
from dotenv import load_dotenv
load_dotenv()

class Extractor:
    def __init__(self):
        self.client = Groq(api_key=os.environ["GROQ_API_KEY"])

    def run(self, pages: list[dict], target: str) -> list[dict]:
        facts = []
        for page in pages:
            prompt = f"""Extract key facts about {target} from this text.
Return a JSON array of objects with keys: "text" (the fact), "confidence" (0.0-1.0), "source".
Text: {page['text'][:2000]}
Source URL: {page['url']}
Return ONLY valid JSON array, no explanation."""
            try:
                resp = self.client.chat.completions.create(
                    model="llama-3.3-70b-versatile",
                    messages=[{"role":"user","content":prompt}],
                    temperature=0.2
                )
                content = resp.choices[0].message.content.strip()
                start = content.find("[")
                end = content.rfind("]") + 1
                if start != -1 and end > start:
                    extracted = json.loads(content[start:end])
                    for f in extracted:
                        f["source"] = page["url"]
                        facts.append(f)
            except Exception as e:
                print(f"Extractor error: {e}")
        return facts
