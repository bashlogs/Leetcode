class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums)
        seen = set(nums)

        for i in range(2 ** n):
            candidate = bin(i)[2:].zfill(n)
            if candidate not in seen:
                return candidate