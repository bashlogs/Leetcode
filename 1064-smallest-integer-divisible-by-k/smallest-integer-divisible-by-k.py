class Solution:
    def smallestRepunitDivByK(self, K: int) -> int:
        remainder = 0
        for n in range(1,K+1):
            remainder = (remainder*10+1) % K
            if remainder == 0:
                return n
        return -1