import requests

def search(query: str) -> str:
    url = "https://api.duckduckgo.com/"
    params = {"q": query, "format": "json"}
    r = requests.get(url, params=params)
    try:
        return r.json().get("AbstractText") or "No result found"
    except Exception as e:
        return f"Search failed: {e}"
