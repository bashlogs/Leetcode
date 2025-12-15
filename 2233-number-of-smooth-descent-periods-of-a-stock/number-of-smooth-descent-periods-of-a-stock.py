class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        n = len(prices)
        prev = 0
        ans = 0
        for i in range(n):
            if i > 0 and prices[i-1] - prices[i] == 1:
                prev += 1
                ans += prev
            else:
                prev = 1
                ans += 1
        
        return ans