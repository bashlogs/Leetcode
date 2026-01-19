class Solution:
    def ambiguousCoordinates(self, s: str) -> List[str]:
        def valid_int(s):
                return len(s) == 1 or s[0] != '0'
            
        def valid_decimal(left, right):
            return valid_int(left) and right[-1] != '0'

        def pointer(string):
            comb = []
            if len(string) == 1:
                return [string]
            
            for i in range(1, len(string)):
                str1 = string[:i]
                str2 = string[i:]
                
                if not valid_decimal(str1, str2):
                    continue

                if int(str1) == 0:
                    if int(str2) != 0:
                        comb.append(f'{str1}.{str2}')
                    break
                elif len(str2) > 0 and int(str2) == 0:
                    continue
                elif str2 == "":
                    comb.append(f'{str1}')
                else:
                    comb.append(f'{str1}.{str2}')

            if valid_int(string):
                comb.append(string)

            return comb
        
        s = s[1:len(s)-1]

        ans = set()

        for i in range(1, len(s)):
            first = s[:i]
            second = s[i:]

            for first_point in pointer(first):
                num1 = first_point
                for second_point in pointer(second):
                    num2 = second_point
                    temp = f"({num1}, {num2})"
                    ans.add(temp)

        return list(ans)