class Solution:
    def findMin(self, nums: List[int]) -> int:
        min = float('inf')

        for i in nums:
            if i < min:
                min = i
        
        return min