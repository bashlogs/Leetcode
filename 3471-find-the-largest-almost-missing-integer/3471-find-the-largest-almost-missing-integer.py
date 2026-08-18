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
        window = defaultdict(int)

        for i in range(len(nums)):
            if i - k >= 0:
                window[nums[i-k]] -= 1
                if window[nums[i-k]] == 0:
                    del window[nums[i-k]]
                    
            window[nums[i]] += 1

            if (i+1) - k >= 0:
                for key in window.keys():
                    counter[key] += 1

        print(counter)
        ans = -1
        for key, val in counter.items():
            if val == 1:
                ans = max(ans, key)
        
        return ans


            