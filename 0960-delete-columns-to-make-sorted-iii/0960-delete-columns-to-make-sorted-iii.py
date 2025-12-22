class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        m = len(strs[0])
        dp = [1] * m

        for i in range(m-2, -1, -1):
            for j in range(i+1, m):
                if all(row[i] <= row[j] for row in strs):
                    dp[i] = max(dp[i], 1 + dp[j])
        
        return m - max(dp)