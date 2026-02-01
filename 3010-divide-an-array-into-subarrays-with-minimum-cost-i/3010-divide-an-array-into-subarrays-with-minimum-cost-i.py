class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        
        total = nums[0]
        nums.pop(0)
        nums.sort()

        total += nums[0] + nums[1]
        return total
        

