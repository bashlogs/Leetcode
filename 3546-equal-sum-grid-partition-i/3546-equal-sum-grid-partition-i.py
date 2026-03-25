class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        n = len(grid)
        m = len(grid[0])

        arr1 = [0] * n
        arr2 = [0] * m

        for i in range(n):
            arr1[i] = sum(grid[i])
        
        for i in range(m):
            total = 0
            for j in range(n):
                total += grid[j][i]
            
            arr2[i] = total
        
        total_arr1 = sum(arr1)
        total_arr2 = sum(arr2)
        curr_arr1 = 0
        curr_arr2 = 0

        for i in range(n):
            curr_arr1 += arr1[i]
            total_arr1 -= arr1[i]

            if curr_arr1 == total_arr1:
                return True
        
        for i in range(m):
            curr_arr2 += arr2[i]
            total_arr2 -= arr2[i]

            if curr_arr2 == total_arr2:
                return True

        return False