from bs4 import BeautifulSoup
import json
import re

with open('crawled_data/home.html', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

print("Title:", soup.title.string if soup.title else None)

# Find top level elements
body = soup.find('body')
if body:
    print("Body classes:", body.get('class'))
    blocks = body.find_all('div', class_='wp-site-blocks')
    root = blocks[0] if blocks else body
    
    # Let's inspect headers, navigations, sections
    headers = soup.find_all('header')
    print(f"Headers found: {len(headers)}")
    for h in headers:
        print("Header classes:", h.get('class'))
        
    footers = soup.find_all('footer')
    print(f"Footers found: {len(footers)}")
    for ft in footers:
        print("Footer classes:", ft.get('class'))

    # Let's see the structure of gutenverse sections or wp-block sections
    guten_sections = soup.find_all('section')
    print(f"Sections found: {len(guten_sections)}")
    for i, s in enumerate(guten_sections):
        headings = [h.get_text().strip() for h in s.find_all(['h1', 'h2', 'h3', 'h4'])]
        print(f"Section {i+1} [classes: {' '.join(s.get('class', []))}]: Headings: {headings[:3]}")

