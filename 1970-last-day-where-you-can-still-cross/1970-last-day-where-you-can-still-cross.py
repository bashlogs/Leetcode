class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        parent = {}
        rank = {}

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            px, py = find(x), find(y)
            if px == py:
                return
            if rank[px] < rank[py]:
                parent[px] = py
            else:
                parent[py] = px
                if rank[px] == rank[py]:
                    rank[px] += 1

        TOP = (-1, -1)
        BOTTOM = (-2, -2)

        parent[TOP] = TOP
        parent[BOTTOM] = BOTTOM
        rank[TOP] = rank[BOTTOM] = 0

        grid = [[1] * col for _ in range(row)]  

        directions = [(0,1),(0,-1),(1,0),(-1,0)]

        for day in range(len(cells) - 1, -1, -1):
            r, c = cells[day]
            r -= 1
            c -= 1
            grid[r][c] = 0 

            parent[(r, c)] = (r, c)
            rank[(r, c)] = 0

            if r == 0:
                union((r, c), TOP)
            if r == row - 1:
                union((r, c), BOTTOM)

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < row and 0 <= nc < col and grid[nr][nc] == 0:
                    union((r, c), (nr, nc))

            if find(TOP) == find(BOTTOM):
                return day

        return 0
