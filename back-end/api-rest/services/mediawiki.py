import requests

WIKI_API = "https://mg.wikipedia.org/w/api.php"
HEADERS = {
    "User-Agent": "MalagasyNLP/1.0 (student-project)"
}

def fetch_words_by_prefix(prefix, limit=10):
    params = {
        "action": "query",
        "list": "prefixsearch",
        "pssearch": prefix,
        "pslimit": limit,
        "format": "json"
    }

    try:
        r = requests.get(WIKI_API, params=params, headers=HEADERS, timeout=10)

        if r.status_code != 200:
            return []

        data = r.json()

        words = []
        for item in data.get("query", {}).get("prefixsearch", []):
            title = item["title"].lower()
            for w in title.split():
                if w.startswith(prefix) and w.isalpha():
                    words.append(w)

        return list(set(words))

    except Exception:
        return []
