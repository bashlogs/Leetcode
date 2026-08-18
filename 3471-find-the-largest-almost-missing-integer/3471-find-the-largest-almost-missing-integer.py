class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        """
        k = 3
        pos = 2
        len = 5


        left = 0
        right = 5

        subarray = min(pos, k) + min(pos + k, len) 

        3 = 1 

        """
        counter = defaultdict(int)
        for i in range(k - 1, len(nums)):
            
            visited = set()

            for j in range((i+1) - k, i+1):
                if nums[j] not in visited:
                    counter[nums[j]] += 1
                    visited.add(nums[j])
        
        ans = -1
        for key, val in counter.items():
            if val == 1:
                ans = max(ans, key)
        
        return ans


            