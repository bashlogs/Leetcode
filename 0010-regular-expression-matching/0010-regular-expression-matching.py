class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
        dp[len(s)][len(p)] = True

        for j in range(len(p) - 2, -1, -1):
            if p[j + 1] == '*':
                dp[len(s)][j] = dp[len(s)][j + 2]

        for i in range(len(s) - 1, -1, -1):
            for j in range(len(p) - 1, -1, -1):
                match = s[i] == p[j] or p[j] == '.'

                if j + 1 < len(p) and p[j+1] == "*":
                    dp[i][j] = dp[i][j+2] or (match and dp[i+1][j])
                else:
                    dp[i][j] = match and dp[i+1][j+1]
                
        return dp[0][0]