import os

pages_dir = "crawled_data/pages"
for fname in sorted(os.listdir(pages_dir)):
    if fname.endswith(".md"):
        path = os.path.join(pages_dir, fname)
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
        lines = [line.strip() for line in content.split("\n") if line.strip()]
        headings = [line for line in lines if line.startswith("#") or line.startswith("**")]
        print(f"=== {fname} ({len(lines)} lines) ===")
        print("Headings / key points sample:")
        for h in headings[:8]:
            print("  ", h[:90])
        print()
