class Solution:
    def checkOnesSegment(self, s: str) -> bool: 
        one = False
        prev = False

        for i in range(len(s)):
            if s[i] == '1':
                if prev == True:
                    return False
                else:
                    one = True
            else:
                if one == True:
                    prev = True

        return True