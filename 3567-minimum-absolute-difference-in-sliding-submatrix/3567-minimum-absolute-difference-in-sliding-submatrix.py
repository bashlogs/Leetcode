class Solution:
    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        rows, cols = m - k + 1, n - k + 1

        ans = [[0] * cols for _ in range(rows)]

        for i in range(rows):
            for j in range(cols):
                vals = []

                for x in range(i, i + k):
                    for y in range(j, j + k):
                        vals.append(grid[x][y])

                vals.sort()

                best = float('inf')
                for t in range(1, len(vals)):
                    if vals[t] != vals[t - 1]:
                        best = min(best, vals[t] - vals[t - 1])

                ans[i][j] = 0 if best == float('inf') else best

        return ans