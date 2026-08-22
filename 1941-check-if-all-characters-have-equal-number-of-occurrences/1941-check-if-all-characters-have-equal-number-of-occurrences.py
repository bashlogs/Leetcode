class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        counter = Counter(s)
        prev = None

        for key, val in counter.items():
            if prev is None:
                prev = val
                continue
            
            if val != prev:
                return False
            
        return True
