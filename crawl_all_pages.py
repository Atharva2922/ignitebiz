import asyncio
import os
import json
from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig, CacheMode

PAGES = [
    ("about", "https://ignitebizai.com/about/"),
    ("psychometric_12d", "https://ignitebizai.com/12-dimension-comprehensive-psychometric-test-2/"),
    ("iris_test", "https://ignitebizai.com/eye-2-i-iris-analysis-comprehensive-psychometric-test/"),
    ("awards", "https://ignitebizai.com/business-awards-ideas/"),
    ("business_mastery", "https://ignitebizai.com/business-mastery-with-ai/"),
    ("c_suite", "https://ignitebizai.com/c-suite-services/"),
    ("venture_architect", "https://ignitebizai.com/venture-architect-ecosystem-strategist-for-academia-beyond/"),
    ("investor_partners", "https://ignitebizai.com/investor-partners/"),
    ("focus_domain", "https://ignitebizai.com/focus-domain/"),
    ("ai_life_manager", "https://ignitebizai.com/ai-life-manager/"),
    ("ai_general_workshop", "https://ignitebizai.com/ai-life-manager-2/"),
    ("contact", "https://ignitebizai.com/contact/")
]

async def crawl_all():
    browser_config = BrowserConfig(headless=True, verbose=False)
    run_config = CrawlerRunConfig(cache_mode=CacheMode.BYPASS, delay_before_return_html=2.0)
    
    os.makedirs("crawled_data/pages", exist_ok=True)
    
    async with AsyncWebCrawler(config=browser_config) as crawler:
        for name, url in PAGES:
            print(f"Crawling {name}: {url}...")
            try:
                res = await crawler.arun(url=url, config=run_config)
                if res.success:
                    with open(f"crawled_data/pages/{name}.md", "w", encoding="utf-8") as f:
                        f.write(res.markdown.raw_markdown if hasattr(res.markdown, 'raw_markdown') else str(res.markdown))
                    with open(f"crawled_data/pages/{name}.html", "w", encoding="utf-8") as f:
                        f.write(res.html or "")
                    print(f"  -> Saved {name}")
                else:
                    print(f"  -> Failed: {res.error_message}")
            except Exception as e:
                print(f"  -> Error crawling {name}: {e}")

if __name__ == "__main__":
    asyncio.run(crawl_all())
