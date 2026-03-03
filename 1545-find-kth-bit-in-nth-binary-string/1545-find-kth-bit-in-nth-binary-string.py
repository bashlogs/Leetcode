class Solution:
    def invert(self, s: str) -> str:
        return ''.join('1' if char == '0' else '0' for char in s)

    def findKthBit(self, n: int, k: int) -> str:
        s = "0"
        for i in range(1, n):
            s = s + "1" + self.invert(s)[::-1]

        return s[k-1]