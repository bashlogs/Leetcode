class Solution:
    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
        n = len(bottomLeft)
        max_side = 0

        for i in range(n - 1):
            for j in range(i+1, n):
                max_x = max(bottomLeft[i][0], bottomLeft[j][0])
                max_y = max(bottomLeft[i][1], bottomLeft[j][1])

                min_x = min(topRight[i][0], topRight[j][0])
                min_y = min(topRight[i][1], topRight[j][1])

                if max_x < min_x and max_y < min_y:
                    width = min_x - max_x
                    height = min_y - max_y

                    max_side = max(max_side, min(width, height))
        
        return max_side ** 2