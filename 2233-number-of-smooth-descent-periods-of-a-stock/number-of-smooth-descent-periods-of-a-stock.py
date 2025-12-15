class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        n = len(prices)
        new_prices = [1] * n

        for i in range(1, n):
            if prices[i-1] - prices[i] == 1:
                new_prices[i] = new_prices[i-1] + 1
        
        return sum(new_prices)