import re

class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        
        category = [[] for _ in range(4)]
        
        pattern = r'^[A-Za-z0-9_]+$'  

        for i in range(len(code)):
            if (re.match(pattern, code[i])) and isActive[i]:
                if businessLine[i] == "electronics":
                    category[0].append(code[i])
                elif businessLine[i] == "grocery": 
                    category[1].append(code[i])
                elif businessLine[i] == "pharmacy": 
                    category[2].append(code[i])
                elif businessLine[i] == "restaurant": 
                    category[3].append(code[i])

        ans = []

        for i in range(len(category)):
            category[i].sort()
            ans += category[i]

        return ans