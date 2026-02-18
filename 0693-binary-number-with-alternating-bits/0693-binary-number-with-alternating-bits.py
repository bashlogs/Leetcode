class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        
        flag = n & 1
        while n:
            bit = n & 1
            if flag == bit:
                flag = 1 if flag == 0 else 0
                n = n >> 1
            else:
                return False

        return True