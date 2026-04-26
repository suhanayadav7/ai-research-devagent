import urllib.request
import urllib.parse
import json

class SearchTool:
    def query(self, gaps: list[str], target: str) -> list[str]:
        urls = []
        for gap in gaps[:3]:
            query = f"{target} {gap}".replace(" ", "+")
            search_url = f"https://html.duckduckgo.com/html/?q={urllib.parse.quote(target+' '+gap)}"
            urls.append(search_url)
        return urls
