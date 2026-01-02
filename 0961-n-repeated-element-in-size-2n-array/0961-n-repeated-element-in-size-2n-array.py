class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        times = len(nums) // 2

        hmap = defaultdict(int)

        for num in nums:
            hmap[num] += 1
            if hmap[num] == times:
                return num
        
        return -1

