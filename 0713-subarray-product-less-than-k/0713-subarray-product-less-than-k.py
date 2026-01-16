class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        total = 0

        for i in range(1, len(nums)):
            nums[i] *= nums[i-1] 
        
        j = 0

        for i in range(len(nums)):
            if nums[i] < k:
                total += (i + 1)
            else:
                while j < i:
                    temp = nums[i] // nums[j]
                    if temp < k:
                        total += (i - j)
                        break
                    else:
                        j += 1

        return total