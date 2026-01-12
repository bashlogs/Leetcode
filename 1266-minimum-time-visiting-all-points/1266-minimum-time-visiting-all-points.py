class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        
        curr = points[0]
        total = 0
        
        for point in points:
            total += max(abs(curr[0] - point[0]), abs(curr[1] - point[1]))
            curr = point
        
        return total