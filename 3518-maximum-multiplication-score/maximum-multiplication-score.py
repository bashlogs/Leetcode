class Solution:
    def maxScore(self, a: List[int], b: List[int]) -> int:
        INF = float("-inf")

        dp = [[INF] * (len(b) + 1) for _ in range(len(a) + 1)]

        for j in range(len(b) + 1):
            dp[0][j] = 0
    
        for i in range(1, len(a) + 1):
            for j in range(i, len(b) + 1):
                dp[i][j] = max(dp[i-1][j-1] + a[i-1] * b[j-1], dp[i][j-1])

        return dp[len(a)][len(b)]