class Solution:
    def numSteps(self, s: str) -> int:
        
        count = 0

        while (s != "1"):
            if int(s) % 2 == 0:
                s = bin(int(s, 2) // 2)[2:]
            else:
                s = bin(int(s, 2) + 1)[2:]
        
            count += 1

        return count