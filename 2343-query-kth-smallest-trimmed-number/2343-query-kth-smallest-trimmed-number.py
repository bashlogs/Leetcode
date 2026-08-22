class Solution:
    def smallestTrimmedNumbers(self, nums: List[str], queries: List[List[int]]) -> List[int]:
        ans = []
        cache = {}
        for k, l in queries:

            trimmed_nums = []

            if l in cache:
                trimmed_nums = cache[l]
            else:
                for i in range(len(nums)):
                    trimmed_nums.append((int(nums[i][len(nums[i])-l:len(nums[i])]), i))
                
                trimmed_nums.sort(key=lambda x: (x[0], x[1]))
                cache[l] = trimmed_nums
            
            ans.append(trimmed_nums[k-1][1])            

        return ans
