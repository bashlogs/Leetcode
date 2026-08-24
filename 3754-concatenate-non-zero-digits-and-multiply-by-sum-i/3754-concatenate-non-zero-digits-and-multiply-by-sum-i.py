class Solution:
    def sumAndMultiply(self, n: int) -> int:
        nums = 0
        sums = 0
        n = str(n)
        
        for i in range(len(n)):
            if n[i] != '0':
                temp = int(n[i])
                nums *= 10
                nums += temp
                sums += temp
        
        return nums * sums
