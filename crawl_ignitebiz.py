import asyncio
import json
import os
from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig, CacheMode

async def crawl_site(url: str, output_prefix: str):
    browser_config = BrowserConfig(headless=True, verbose=True)
    run_config = CrawlerRunConfig(
        cache_mode=CacheMode.BYPASS,
        delay_before_return_html=3.0,
    )

    os.makedirs("crawled_data", exist_ok=True)

    async with AsyncWebCrawler(config=browser_config) as crawler:
        print(f"Crawling {url}...")
        result = await crawler.arun(url=url, config=run_config)
        
        if result.success:
            print(f"Successfully crawled: {result.url}")
            
            # Save markdown
            md_path = os.path.join("crawled_data", f"{output_prefix}.md")
            with open(md_path, "w", encoding="utf-8") as f:
                f.write(result.markdown.raw_markdown if hasattr(result.markdown, 'raw_markdown') else str(result.markdown))
            
            # Save html
            html_path = os.path.join("crawled_data", f"{output_prefix}.html")
            with open(html_path, "w", encoding="utf-8") as f:
                f.write(result.html or "")
                
            # Save cleaned html if available
            cleaned_html_path = os.path.join("crawled_data", f"{output_prefix}_cleaned.html")
            if hasattr(result, 'cleaned_html') and result.cleaned_html:
                with open(cleaned_html_path, "w", encoding="utf-8") as f:
                    f.write(result.cleaned_html)

            # Save metadata & links & media
            meta = {
                "url": result.url,
                "status_code": result.status_code,
                "links": result.links if hasattr(result, 'links') else {},
                "media": result.media if hasattr(result, 'media') else {},
            }
            meta_path = os.path.join("crawled_data", f"{output_prefix}_meta.json")
            with open(meta_path, "w", encoding="utf-8") as f:
                json.dump(meta, f, indent=2, default=str)
                
            print(f"Saved {output_prefix} files to crawled_data/")
            return meta
        else:
            print(f"Crawl failed for {url}: {result.error_message}")
            return None

async def main():
    meta = await crawl_site("https://ignitebizai.com/", "home")
    if meta and "links" in meta:
        internal_links = meta["links"].get("internal", [])
        print(f"Discovered internal links: {len(internal_links)}")
        for idx, link in enumerate(internal_links[:10]):
            href = link.get("href") if isinstance(link, dict) else str(link)
            print(f"  Link {idx+1}: {href}")

if __name__ == "__main__":
    asyncio.run(main())
