class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n
        for i in range(len(nums)):
            ans = nums[i]
            if nums[i] > 0:
                ans = nums[(i + nums[i]) % n]
            elif nums[i] < 0:
                ans = nums[(nums[i] + i) % n]

            result[i] = ans
        
        return result