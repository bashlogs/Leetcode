class Solution:
    def sumAndMultiply(self, n: int) -> int:
        nums = 0
        sums = 0
        n = str(n)
        for i in range(len(n)):
            if n[i] != '0':
                nums *= 10
                nums += int(n[i])
                sums += int(n[i])
        
        return nums * sums
