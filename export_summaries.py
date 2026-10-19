import os
import json

def read_file(path):
    with open(path, "r", encoding="utf-8", errors="replace") as f:
        return f.read()

pages_info = {}
for fname in os.listdir("crawled_data/pages"):
    if fname.endswith(".md"):
        content = read_file(os.path.join("crawled_data/pages", fname))
        pages_info[fname] = content

with open("crawled_data/pages_summary.json", "w", encoding="utf-8") as f:
    json.dump({k: v[:2000] for k, v in pages_info.items()}, f, indent=2)

print("Saved pages_summary.json")
