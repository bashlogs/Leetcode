class Solution:
    def getRow(self, rowIndex: int) -> List[int]:

        dp = [0] * (rowIndex + 1)
        dp[0] = 1

        for i in range(rowIndex + 1):
            prev = dp[:]

            for j in range(1, i+1):
                prev[j] = dp[j-1] + dp[j]

            dp = prev

        return dp