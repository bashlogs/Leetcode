class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        neg = 0
        ans = 0
        minx = float('inf')

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                ans += abs(matrix[i][j])
                if matrix[i][j] < 0:
                    neg += 1
                
                minx = min(minx, abs(matrix[i][j]))
        
        return ans if neg % 2 == 0 else ans - 2*minx
