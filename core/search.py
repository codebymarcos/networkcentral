from ddgs import DDGS

class search:
    def __init__(self, entry: str) -> None:
        self.results = []
        self.entry = entry
        
    def search(self) -> str:
        with DDGS() as ddgs:
            self.results = ddgs.text(self.entry, max_results=5)
        return '\n'.join(f"{result['title']} {result['href']}" for result in self.results)

if __name__ == "__main__":
    s = search("Python programming")
    results_str = s.search()
    print(results_str)