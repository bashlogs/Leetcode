class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        total = 0

        for ch in columnTitle:
            total += total * 25 + (ord(ch) - (ord('A') - 1))

        return total