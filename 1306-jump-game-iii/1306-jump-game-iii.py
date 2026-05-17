class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        left = {}
        right = {}
        def solve(curr):
            if curr in left and curr in right:
                return False
            
            if arr[curr] == 0:
                return True
            
            if curr not in left and arr[curr] <= curr:
                left[curr] = False
                left[curr] = solve(curr - arr[curr])
            
            if curr not in right and curr + arr[curr] < len(arr):
                right[curr] = False
                right[curr] = solve(curr + arr[curr])
            
            if curr not in left:
                left[curr] = False
            
            if curr not in right:
                right[curr] = False
                
            return left[curr] or right[curr]
            
        return solve(start)