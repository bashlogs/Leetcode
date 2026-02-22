class Solution:
    def binaryGap(self, n: int) -> int:
        
        s = bin(n)[2:]

        ans = 0
        prev = -1
        for i in range(len(s)):
            if s[i] == '1':
                if prev != -1:
                    ans = max(i-prev, ans)
                
                prev = i
        
        return ans