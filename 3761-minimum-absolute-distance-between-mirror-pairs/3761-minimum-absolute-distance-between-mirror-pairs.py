import bisect

class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        def reverse(c):
            temp = str(c)[::-1]
            return int(temp)
        
        number = defaultdict(list)
        for i in range(len(nums)):
            number[nums[i]].append(i)

        min_dist = float('inf')
        for i in range(len(nums)):
            reverse_num = reverse(nums[i])
            if reverse_num in number:
                result = number[reverse_num]
                pos = bisect.bisect(result, i)

                if pos < len(result):
                    min_dist = min(min_dist, abs(i - result[pos]))

        return min_dist if min_dist != float('inf') else -1
