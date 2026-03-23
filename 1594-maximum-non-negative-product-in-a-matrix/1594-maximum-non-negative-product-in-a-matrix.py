class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        MOD = 10**9 + 7
        INF = 10**9 + 7
        grid2 = [[[-INF, INF] for _ in range(m)] for c in range(n)]

        for i in range(n):
            for j in range(m):
                curr = grid[i][j]
                if i > 0 and j > 0:
                    neg = min(grid2[i-1][j][1], grid2[i][j-1][1])
                    pos = max(grid2[i-1][j][0], grid2[i][j-1][0])

                    if curr < 0:
                        grid2[i][j][0] = neg * curr
                        grid2[i][j][1] = pos * curr
                    else:
                        grid2[i][j][0] = pos * curr
                        grid2[i][j][1] = neg * curr
                elif j > 0:
                    if curr < 0:
                        grid2[i][j][0] = grid2[i][j-1][1] * curr
                        grid2[i][j][1] = grid2[i][j-1][0] * curr
                    else:
                        grid2[i][j][0] = grid2[i][j-1][0] * curr
                        grid2[i][j][1] = grid2[i][j-1][1] * curr
                elif i > 0:
                    if curr < 0:
                        grid2[i][j][0] = grid2[i-1][j][1] * curr
                        grid2[i][j][1] = grid2[i-1][j][0] * curr
                    else:
                        grid2[i][j][0] = grid2[i-1][j][0] * curr
                        grid2[i][j][1] = grid2[i-1][j][1] * curr
                else:
                    if curr < 0:
                        grid2[i][j][1] = curr
                    else:
                        grid2[i][j][0] = curr
                    
        if grid2[n-1][m-1][0] < 0:
            return -1
        else:
            return grid2[n-1][m-1][0] % MOD