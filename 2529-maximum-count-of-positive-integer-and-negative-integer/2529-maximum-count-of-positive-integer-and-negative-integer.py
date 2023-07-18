class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        negative = 0
        positive = 0
        i = len(nums)
        for n in range(i):
            if(nums[n] < 0):
                negative += 1
            elif(nums[n] > 0):
                positive += 1
        
        if(negative >= positive):
            return negative
        else:
            return positive