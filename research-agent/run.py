import asyncio
import sys
import os
from agent.orchestrator import ResearchAgent

async def main():
    target = " ".join(sys.argv[1:]) if len(sys.argv) > 1 else "Jensen Huang"
    agent = ResearchAgent(target)
    report = await agent.run(max_cycles=3)
    print("\n" + "="*60)
    print(report)
    print("="*60)
    os.makedirs("output", exist_ok=True)
    filename = f"output/{target.replace(' ','_').lower()}_report.md"
    with open(filename, "w") as f:
        f.write(report)
    print(f"\n[SAVED] Report saved to {filename}")

asyncio.run(main())
