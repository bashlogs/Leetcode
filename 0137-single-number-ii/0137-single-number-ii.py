class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        map = defaultdict(int)

        for num in nums:
            map[num] += 1
        
        for k, v in map.items():
            if v == 1:
                return k
                