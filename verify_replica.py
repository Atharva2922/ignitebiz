import os
import re
from html.parser import HTMLParser
try:
    from bs4 import BeautifulSoup
    USE_BS4 = True
except ImportError:
    USE_BS4 = False

html_files = [f for f in os.listdir('.') if f.endswith('.html')]
print(f"Total HTML files to verify: {len(html_files)}")

all_passed = True
total_images_checked = 0
total_links_checked = 0

class FallbackParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []
        self.images = []
        self.title = None
        self._in_title = False

    def handle_starttag(self, tag, attrs):
        attrs_dict = dict(attrs)
        if tag == 'title':
            self._in_title = True
        elif tag == 'a' and 'href' in attrs_dict:
            self.links.append(attrs_dict['href'])
        elif tag == 'img' and 'src' in attrs_dict:
            self.images.append(attrs_dict['src'])

    def handle_endtag(self, tag):
        if tag == 'title':
            self._in_title = False

    def handle_data(self, data):
        if self._in_title and not self.title:
            self.title = data.strip()

for hfile in html_files:
    print(f"\n--- Checking {hfile} ---")
    with open(hfile, 'r', encoding='utf-8') as f:
        content = f.read()

    if USE_BS4:
        soup = BeautifulSoup(content, 'html.parser')
        title = soup.title.string if soup.title else None
        links = [a['href'] for a in soup.find_all('a', href=True)]
        imgs = [img['src'] for img in soup.find_all('img', src=True)]
    else:
        parser = FallbackParser()
        parser.feed(content)
        title = parser.title
        links = parser.links
        imgs = parser.images

    # 1. Check title
    print(f"  Title: {title}")
    if not title:
        print("  [ERROR] Missing title!")
        all_passed = False

    # 2. Check internal links
    for l in links:
        if not l.startswith('http') and not l.startswith('#') and not l.startswith('mailto:') and not l.startswith('tel:') and not l.startswith('javascript:'):
            total_links_checked += 1
            clean_link = l.split('#')[0].split('?')[0]
            if clean_link and not os.path.exists(clean_link):
                print(f"  [ERROR] Broken internal link: {l} in {hfile}")
                all_passed = False

    # 3. Check images
    for img in imgs:
        if not img.startswith('http') and not img.startswith('//') and not img.startswith('data:'):
            total_images_checked += 1
            clean_img = img.split('?')[0]
            if not os.path.exists(clean_img):
                print(f"  [WARNING] Local image missing: {img} in {hfile}")
                all_passed = False

print(f"\nVerification Complete!")
print(f"Total HTML files: {len(html_files)}")
print(f"Total local links verified: {total_links_checked}")
print(f"Total local images verified: {total_images_checked}")
print(f"Status: {'ALL CHECKS PASSED PERFECTLY!' if all_passed else 'SOME ISSUES FOUND'}")
