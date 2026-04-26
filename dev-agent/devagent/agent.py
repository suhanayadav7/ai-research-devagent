import os
from groq import Groq
from dotenv import load_dotenv
load_dotenv()

client = Groq(api_key=os.environ["GROQ_API_KEY"])
MODEL = "llama-3.3-70b-versatile"

def ask(prompt):
    resp = client.chat.completions.create(
        model=MODEL,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2,
        max_tokens=2000
    )
    return resp.choices[0].message.content

def read_file(path):
    with open(path) as f:
        return f.read()

def explain_code(path):
    src = read_file(path)
    return ask(f"Explain this code clearly. Cover what it does, each function, and potential issues:\n\n{src}")

def debug_code(path, error):
    src = read_file(path)
    return ask(f"Debug this error and provide a fix.\n\nError: {error}\n\nCode:\n{src}\n\nGive: 1) Root cause 2) Fix 3) Prevention")

def generate_docs(path):
    src = read_file(path)
    result = ask(f"Add detailed docstrings to every function in this Python code. Return the complete file:\n\n{src}")
    out = path.replace(".py", "_documented.py")
    with open(out, "w") as f:
        f.write(result)
    return f"Saved to {out}\n\n{result}"

def write_tests(path):
    src = read_file(path)
    result = ask(f"Write comprehensive pytest unit tests for all functions. Include edge cases. Return complete test file:\n\n{src}")
    out = path.replace(".py", "_test.py")
    with open(out, "w") as f:
        f.write(result)
    return f"Saved to {out}\n\n{result}"

def review_code(path):
    src = read_file(path)
    return ask(f"Do a thorough code review. Flag bugs, security issues, performance problems. Rate each as [CRITICAL] [WARNING] [SUGGESTION]:\n\n{src}")
