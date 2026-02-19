class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        
        """

        00110011

        001234

        """

        def func(index, s):
            flag = False
            zero = 0
            one = 0

            for i in range(index, len(s)):
                if flag and s[i] == s[index]:
                    break
                elif s[i] != s[index]:
                    flag = True

                if s[i] == '0':
                    zero += 1
                else:
                    one += 1
            
            return min(zero, one)
                

        prev = None
        first, second = 0, 0
        for i in range(len(s)):
            if s[i] == '0' and prev != s[i]:
                first += func(i, s)
            elif s[i] == '1' and prev != s[i]:
                second += func(i, s)

            prev = s[i]
        
        return first + second

