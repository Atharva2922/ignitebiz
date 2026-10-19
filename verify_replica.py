import os
import re
from bs4 import BeautifulSoup

html_files = [f for f in os.listdir('.') if f.endswith('.html')]
print(f"Total HTML files to verify: {len(html_files)}")

all_passed = True
total_images_checked = 0
total_links_checked = 0

for hfile in html_files:
    print(f"\n--- Checking {hfile} ---")
    with open(hfile, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')
    
    # 1. Check title
    title = soup.title.string if soup.title else None
    print(f"  Title: {title}")
    if not title:
        print("  [ERROR] Missing title!")
        all_passed = False

    # 2. Check internal links
    links = [a['href'] for a in soup.find_all('a', href=True)]
    for l in links:
        if not l.startswith('http') and not l.startswith('#') and not l.startswith('mailto:') and not l.startswith('tel:'):
            total_links_checked += 1
            clean_link = l.split('#')[0]
            if clean_link and not os.path.exists(clean_link):
                print(f"  [ERROR] Broken internal link: {l} in {hfile}")
                all_passed = False

    # 3. Check images
    imgs = [img['src'] for img in soup.find_all('img', src=True)]
    for img in imgs:
        if not img.startswith('http') and not img.startswith('//'):
            total_images_checked += 1
            if not os.path.exists(img):
                print(f"  [WARNING] Local image missing: {img} in {hfile}")
                all_passed = False

print(f"\nVerification Complete!")
print(f"Total HTML files: {len(html_files)}")
print(f"Total local links verified: {total_links_checked}")
print(f"Total local images verified: {total_images_checked}")
print(f"Status: {'ALL CHECKS PASSED PERFECTLY!' if all_passed else 'SOME ISSUES FOUND'}")
