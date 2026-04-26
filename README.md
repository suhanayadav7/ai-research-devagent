# AI Agent Assignment

## Assignment 1 - Autonomous Research Agent
Researches any founder/CEO autonomously using web browsing + LLM synthesis.

### Run
cd research-agent
pip3 install groq chromadb playwright python-dotenv
python3 -m playwright install chromium
python3 run.py "Jensen Huang"

## Assignment 2 - Dev Workflow Agent
AI-powered code explanation, debugging, documentation, testing and review.

### Run
cd dev-agent
pip3 install groq python-dotenv
python3 -m devagent.cli explain sample.py
python3 -m devagent.cli review sample.py
python3 -m devagent.cli docs sample.py
python3 -m devagent.cli tests sample.py
python3 -m devagent.cli debug sample.py "your error here"

## Setup
Add your Groq API key to .env in each folder:
GROQ_API_KEY=your_key_here
