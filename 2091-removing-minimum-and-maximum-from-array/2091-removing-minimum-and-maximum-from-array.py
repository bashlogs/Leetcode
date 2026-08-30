class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        """
        right = len(nums) - min(index(a), index(b))
        left = max(index(a), index(b))

        middle = min(index(a), index(b)) + (len(nums) - max(index(a), index(b)))

        return min(right, left, middle)

        """

        index_a = 0
        index_b = 0

        for i in range(len(nums)):
            if nums[index_a] < nums[i]:
                index_a = i
            
            if nums[index_b] > nums[i]:
                index_b = i

        left = max(index_a, index_b) + 1
        right = len(nums) - min(index_a, index_b)
        middle = min(index_a, index_b) + 1 + (len(nums) - max(index_a, index_b))

        return min(left, right, middle)