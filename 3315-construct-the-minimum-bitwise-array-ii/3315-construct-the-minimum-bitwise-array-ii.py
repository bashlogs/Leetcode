class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums)

        for c, num in enumerate(nums):
            res = -1
            d = 1

            while num & d != 0:
                res = num - d
                d <<= 1

            ans[c] = res
        
        return ans