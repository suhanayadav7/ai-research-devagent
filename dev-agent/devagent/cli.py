import sys, os
sys.path.insert(0, os.path.expanduser("~/dev-agent"))
from devagent.agent import explain_code, debug_code, generate_docs, write_tests, review_code

def main():
    if len(sys.argv) < 3:
        print("Usage: python3 -m devagent.cli [explain|debug|docs|tests|review] <file.py>")
        return
    cmd, path = sys.argv[1], sys.argv[2]
    print(f"\n[DEV AGENT] {cmd.upper()} on {path}\n" + "="*60)
    if cmd == "explain":
        print(explain_code(path))
    elif cmd == "debug":
        print(debug_code(path, sys.argv[3] if len(sys.argv) > 3 else "Unknown error"))
    elif cmd == "docs":
        print(generate_docs(path))
    elif cmd == "tests":
        print(write_tests(path))
    elif cmd == "review":
        print(review_code(path))
    print("="*60)

if __name__ == "__main__":
    main()
