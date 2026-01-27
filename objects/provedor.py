import os
import sys

__path__ = os.path.dirname(os.path.abspath(__file__))
__root__ = os.path.dirname(__path__)
sys.path.append(__root__)

from core.search import search
from core.binarization import binarization

class Provider:
    def __init__(self, name: str):
        self.name = name

    def search(self, query: str) -> str:
        try:
            s = search(query)
            results_str = s.search()  # s.search() now returns str
            return self.binarize(results_str)
        except Exception:
            return ""
        
    def binarize(self, text: str) -> str:
        try:
            b = binarization()
            return b.binarize(text)
        except Exception:
            return ""

if __name__ == "__main__":
    provider = Provider("ExampleProvider")
    
    # Get binary search results
    binary_results = provider.search("OpenAI")
    print(binary_results)
        
