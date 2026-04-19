class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        """
        sqrt(c - a**2)
        """
        l, r = 0, int(sqrt(c))
        while l <= r:
            m = l * l + r * r
            if m > c:
                r -= 1
            elif m < c:
                l += 1
            else:
                return True
        
        return False