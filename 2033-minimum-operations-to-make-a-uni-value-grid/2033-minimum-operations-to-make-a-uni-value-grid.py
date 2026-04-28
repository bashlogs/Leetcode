class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        flatgrid = [num for row in grid for num in row]
        rem = flatgrid[0] % x

        for i in flatgrid:
            if i % x != rem:
                return -1
        
        flatgrid.sort()
        median = flatgrid[len(flatgrid) // 2]

        return sum(abs(num - median) // x for num in flatgrid)