class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        hmap1 = defaultdict(int)
        hmap2 = Counter(nums)
        count = 0
        mod = 10**9 + 7

        for i in range(len(nums) - 1):
            temp = nums[i]
            hmap2[temp] -= 1
                
            mul = (temp * 2) % mod
            if hmap1[mul] > 0 and hmap2[mul] > 0:
                count += hmap1[mul] * hmap2[mul]
                count %= mod
            
            hmap1[temp] += 1
        
        return count

