class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        max_len = 0
        i = 0
    
        for j in range(n):
            while nums[j] > nums[i] * k:
                i += 1
            max_len = max(max_len, j - i + 1)
            
        return n - max_len