class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False

        l, h = 0, n ** (1/3)

        while l <= h:
            mid = l + (h - l) // 2
            if 3 ** mid == n:
                return True
            elif 3 ** mid > n:
                h = mid - 1
            else:
                l = mid + 1
        
        return False
