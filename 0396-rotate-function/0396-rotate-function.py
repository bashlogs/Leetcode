class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        """
        4, 3, 2, 6 = 4 * 0, 3 * 1, 2 * 2, 6 * 3 = 
        

        """
        f, n, numSum = 0, len(nums), sum(nums)
        for i, num in enumerate(nums):
            f += i * num
        res = f
        for i in range(n - 1, 0, -1):
            f = f + numSum - n * nums[i]
            res = max(res, f)
        return res