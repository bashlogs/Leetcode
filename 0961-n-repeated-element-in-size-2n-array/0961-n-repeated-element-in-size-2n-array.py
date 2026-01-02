class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        times = len(nums) // 2
        nums.sort()
        count = 0
        index = 0

        for num in nums:
            if num == index:
                count += 1
            else:
                count = 1

            index = num

            if count == times:
                return index
        
        return -1

