class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        pointer = {}

        for i in range(len(nums)):
            pointer[i] = nums[i]
        
        sorted_dict = dict(sorted(pointer.items(), key = lambda x: x[1]))
        nums = [i for i in sorted_dict.keys()]
        ans = float('inf')

        for i in range(len(nums)-2):
            if sorted_dict[nums[i]] == sorted_dict[nums[i+1]] and sorted_dict[nums[i+1]] == sorted_dict[nums[i+2]]:
                ans = min(ans, abs(nums[i] - nums[i+1]) + abs(nums[i+1] - nums[i+2]) + abs(nums[i+2] - nums[i]))
        
        return ans if ans != float('inf') else -1
