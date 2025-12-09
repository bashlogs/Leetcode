class Solution:
    def maximum69Number (self, num: int) -> int:
        s = list(str(num))

        res = num

        for i in range(len(s)):
            if s[i] == '6':
                s[i] = '9'
                res = max(res, int(''.join(s)))
                s[i] = '6'
        
        return res