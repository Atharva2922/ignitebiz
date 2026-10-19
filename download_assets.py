import os
import re
import urllib.request
from bs4 import BeautifulSoup

os.makedirs("assets/images", exist_ok=True)

html_files = ["crawled_data/home.html"]
pages_dir = "crawled_data/pages"
if os.path.exists(pages_dir):
    for f in os.listdir(pages_dir):
        if f.endswith(".html"):
            html_files.append(os.path.join(pages_dir, f))

image_urls = set()

for file_path in html_files:
    with open(file_path, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f.read(), "html.parser")
        for img in soup.find_all("img"):
            src = img.get("src")
            if src and (src.startswith("http://") or src.startswith("https://")):
                image_urls.add(src)

print(f"Total unique images found across all crawled pages: {len(image_urls)}")

downloaded = {}
headers = {'User-Agent': 'Mozilla/5.0'}

for url in sorted(image_urls):
    filename = url.split("?")[0].split("/")[-1]
    # sanitize filename
    filename = re.sub(r'[^a-zA-Z0-9_\.-]', '_', filename)
    if not filename:
        continue
    target_path = os.path.join("assets/images", filename)
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as response, open(target_path, 'wb') as out_file:
            out_file.write(response.read())
        downloaded[url] = f"assets/images/{filename}"
        print(f"Downloaded: {filename}")
    except Exception as e:
        print(f"Failed to download {url}: {e}")

print(f"Downloaded {len(downloaded)} images.")
