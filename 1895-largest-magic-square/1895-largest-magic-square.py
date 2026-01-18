class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        
        n = len(grid)
        m = len(grid[0])

        orig = [row[:] for row in grid]

        col_ps = [[0] * m for _ in range(n)]
        for j in range(m):
            col_ps[0][j] = orig[0][j]
            for i in range(1, n):
                col_ps[i][j] = col_ps[i - 1][j] + orig[i][j]

        def check(grid, size):
            for i in range(n - size + 1):
                for j in range(size - 1, m):

                    curr = grid[i][j] - (grid[i][j - size] if j - size >= 0 else 0)

                    ok = True
                    for r in range(1, size):
                        row_sum = grid[i + r][j] - (grid[i + r][j - size] if j - size >= 0 else 0)
                        if row_sum != curr:
                            ok = False
                            break
                    if not ok:
                        continue

                    d1 = d2 = 0
                    for d in range(size):
                        d1 += orig[i + d][j - size + 1 + d]
                        d2 += orig[i + d][j - d]
                    if d1 != curr or d2 != curr:
                        continue

                    for c in range(j - size + 1, j + 1):
                        col_sum = col_ps[i + size - 1][c] - (col_ps[i - 1][c] if i > 0 else 0)
                        if col_sum != curr:
                            ok = False
                            break

                    if ok:
                        return True

            return False

        for i in range(n):
            for j in range(1, m):
                grid[i][j] += grid[i][j - 1]

        ans = 1
        for size in range(2, min(n, m) + 1):
            if check(grid, size):
                ans = size

        return ans
