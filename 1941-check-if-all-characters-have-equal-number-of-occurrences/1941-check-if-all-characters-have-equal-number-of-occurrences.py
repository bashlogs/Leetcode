class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        counter = Counter(s)
        val = list(counter.values())
        return len(set(val)) == 1
