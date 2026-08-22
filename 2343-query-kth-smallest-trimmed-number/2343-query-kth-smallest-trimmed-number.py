class Solution:
    def smallestTrimmedNumbers(self, nums: List[str], queries: List[List[int]]) -> List[int]:
        ans = []

        for k, l in queries:

            trimmed_nums = []

            for i in range(len(nums)):
                trimmed_nums.append((int(nums[i][len(nums[i])-l:len(nums[i])]), i))
            
            trimmed_nums.sort(key=lambda x: (x[0], x[1]))

            ans.append(trimmed_nums[k-1][1])            

        return ans
