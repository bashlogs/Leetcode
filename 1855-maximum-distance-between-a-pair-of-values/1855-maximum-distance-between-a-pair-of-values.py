class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        """

        55, 100
        5, 10 | 5, 10 | 5, 5


        """
        ans = 0

        for i in range(len(nums1)):

            if i < len(nums2) and nums1[i] > nums2[i]:
                continue

            l, r = i, len(nums2) - 1

            while l <= r:
                m = l + (r - l) // 2
                if nums2[m] < nums1[i]:
                    r = m - 1
                else:
                    l = m + 1

            ans = max(ans, (r - i))

        return ans
