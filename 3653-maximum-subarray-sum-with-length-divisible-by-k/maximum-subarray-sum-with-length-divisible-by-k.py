class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        """

        [1, 3]
        hash = {1: 0}, {3: 1}

        [-1, -3, -6, -10, -15]

        """

        n = len(nums)
        prefixSum = 0
        maxsum = -sys.maxsize
        val = [sys.maxsize // 2] * k
        val[k-1] = 0
        
        for i in range(n):
            prefixSum += nums[i]
            maxsum = max(maxsum, prefixSum - val[i % k])
            val[i%k] = min(val[i%k], prefixSum)
        
        return maxsum
