class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        nums = set(nums)
        i = 1
        while (k * i in nums):
            i += 1
        
        return k * i