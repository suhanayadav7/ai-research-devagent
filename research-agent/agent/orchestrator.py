import asyncio
from agent.tools.memory import MemoryStore
from agent.tools.search import SearchTool
from agent.tools.browser import BrowserTool
from agent.tools.extractor import Extractor
from agent.report import ReportEngine

GOALS = [
    "founding story and early life",
    "career milestones and achievements",
    "philosophy and leadership style",
    "net worth and company valuation",
    "recent news and activity",
    "notable quotes and interviews"
]

class ResearchAgent:
    def __init__(self, target: str):
        self.target = target
        self.memory = MemoryStore()
        self.search = SearchTool()
        self.browser = BrowserTool()
        self.extractor = Extractor()
        self.report_engine = ReportEngine()

    async def run(self, max_cycles=3):
        print(f"\n[PLAN] Researching: {self.target}")
        print(f"[PLAN] Goals: {len(GOALS)} sub-topics\n")

        for cycle in range(max_cycles):
            gaps = [g for g in GOALS if g not in self.memory.covered_goals(GOALS)]
            if not gaps:
                print("[DONE] All goals covered!")
                break
            print(f"[cycle {cycle+1}] Gaps remaining: {len(gaps)}")
            urls = self.search.query(gaps, self.target)
            print(f"[cycle {cycle+1}] Fetching {len(urls)} pages...")
            pages = await self.browser.crawl(urls)
            facts = self.extractor.run(pages, self.target)
            self.memory.upsert(facts)
            print(f"[cycle {cycle+1}] Stored {len(facts)} facts\n")

        print("[REPORT] Synthesizing final report...")
        chunks = self.memory.query_all(GOALS)
        report = self.report_engine.build(chunks, self.target)
        return report
