class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        """
        1 0 1 2
        0 1 1 2
        1 0 0 0
        2 1 2

        0 0 1
        1 1 1
        1 0 1


        """

        m = len(matrix)
        n = len(matrix[0])
        ans = 0

        for row in range(m):
            for col in range(n):
                if matrix[row][col] != 0 and row > 0:
                    matrix[row][col] += matrix[row-1][col]
            
            curr_row = sorted(matrix[row], reverse=True)

            for i in range(n):
                ans = max(ans, curr_row[i] * (i+1))
        
        return ans