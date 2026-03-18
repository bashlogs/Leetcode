class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        
        """

        7 9 18
        8 15 24
        10 23 


        """
        count = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):

                if j > 0:
                    grid[i][j] += grid[i][j-1]
                
                if i > 0:
                    grid[i][j] += grid[i-1][j]

                if i > 0 and j > 0:
                    grid[i][j] -= grid[i-1][j-1]

                if grid[i][j] <= k:
                    count += 1

        return count