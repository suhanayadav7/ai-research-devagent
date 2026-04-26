import asyncio
from playwright.async_api import async_playwright
import re

class BrowserTool:
    async def fetch_page(self, url: str) -> str:
        try:
            async with async_playwright() as p:
                browser = await p.chromium.launch(headless=True)
                page = await browser.new_page()
                await page.goto(url, timeout=15000)
                text = await page.inner_text("body")
                await browser.close()
                return text[:3000]
        except Exception as e:
            return f"Error fetching {url}: {e}"

    async def crawl(self, urls: list[str], depth=1) -> list[dict]:
        pages = []
        for url in urls[:4]:
            text = await self.fetch_page(url)
            pages.append({"url": url, "text": text})
        return pages
