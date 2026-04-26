# AI Research & Dev Agent Suite

> Two production-ready autonomous AI agents built with Python, Groq LLaMA, Playwright, and ChromaDB.

---

## Assignment 1 - Autonomous Research Agent

Researches any founder or CEO by autonomously browsing the web, maintaining memory, detecting coverage gaps, and synthesizing a structured report.

### How it works
1. Decomposes the target into 6 research sub-goals
2. Searches the web using DuckDuckGo (no API key needed)
3. Crawls pages headlessly using Playwright
4. Extracts and stores facts in ChromaDB vector memory
5. Detects uncovered goals and re-searches until complete
6. Synthesizes a full Markdown report using LLaMA 3.3 70B

### Run
    cd research-agent
    pip3 install groq chromadb playwright python-dotenv
    python3 -m playwright install chromium
    echo GROQ_API_KEY=your_key > .env
    python3 run.py Jensen Huang

---

## Assignment 2 - Dev Workflow Agent

AI-powered CLI tool for code understanding, debugging, documentation, testing, and review.

### Commands
- explain : Plain-language explanation of any Python file
- debug   : Root cause analysis and minimal fix for any error
- docs    : Adds docstrings to every function automatically
- tests   : Generates pytest unit tests with edge cases
- review  : Full code review with CRITICAL / WARNING / SUGGESTION ratings

### Run
    cd dev-agent
    pip3 install groq python-dotenv
    echo GROQ_API_KEY=your_key > .env
    python3 -m devagent.cli explain sample.py
    python3 -m devagent.cli review sample.py
    python3 -m devagent.cli docs sample.py
    python3 -m devagent.cli tests sample.py
    python3 -m devagent.cli debug sample.py your error here

---

## Tech Stack
- Groq + LLaMA 3.3 70B : LLM backbone (free, fast)
- Playwright            : Headless browser automation
- ChromaDB             : Vector memory store
- DuckDuckGo           : Free web search, no API key needed
- Python 3.9+          : Core language

---

## Setup
1. Get a free Groq API key at https://console.groq.com
2. Add it to .env in each project folder:
   GROQ_API_KEY=your_key_here
