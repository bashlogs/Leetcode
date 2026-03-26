class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        m = len(grid)
        n = len(grid[0])

        # corner case
        def check_simple_line(line):
            full_sum = sum(line)
            left = 0
            for i in range(len(line) - 1):
                left += line[i]
                delta = left - (full_sum - left)
                if (
                    delta == 0
                    or (delta > 0 and delta in (line[0], line[i]))
                    or (delta < 0 and -delta in (line[i + 1], line[-1]))
                ):
                    return True
            return False

        if m == 1:
            return check_simple_line(grid[0])
        elif n == 1:
            col = [grid[i][0] for i in range(m)]
            return check_simple_line(col)

        c = Counter(
            elem
            for line in grid
            for elem in line
        )
        full_sum = sum(elem * cnt for elem, cnt in c.items())

        def check(lines, c):
            left = 0
            left_c = Counter()
            for i in range(len(lines) - 1):
                left += sum(lines[i])
                left_c.update(lines[i])
                delta = left - (full_sum - left)
                if delta == 0:
                    return True
                
                if delta > 0 and i == 0:
                    # first line
                    if delta in (lines[0][0], lines[0][-1]):
                        return True
                elif delta < 0 and i == len(lines) - 2:
                    # last line
                    if -delta in (lines[-1][0], lines[-1][-1]):
                        return True
                else:
                    # other cases
                    if delta > 0 and delta in left_c:
                        return True
                    elif delta < 0 and (c[-delta] - left_c[-delta]) > 0:
                        return True
            return False
        
        if check(grid, c):
            return True
        
        cols = [
            [grid[i][j] for i in range(m)]
            for j in range(n)
        ]
        return check(cols, c)