class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        n, m = len(mat), len(mat[0])

        pre = [[0] * (m + 1) for _ in range(n + 1)]
        for i in range(n):
            for j in range(m):
                pre[i+1][j+1] = mat[i][j] + pre[i][j+1] + pre[i+1][j] - pre[i][j]

        def get_sum(x1, y1, x2, y2):
            return pre[x2+1][y2+1] - pre[x1][y2+1] - pre[x2+1][y1] + pre[x1][y1]

        ans = 0

        for k in range(1, min(n, m) + 1):
            found = False
            for i in range(n - k + 1):
                for j in range(m - k + 1):
                    if get_sum(i, j, i + k - 1, j + k - 1) <= threshold:
                        found = True
                        break
                if found:
                    break
            if found:
                ans = k
            else:
                break 

        return ans