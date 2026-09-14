from itertools import permutations

class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        
        perm = list(set(permutations(digits, 3)))
        ans = 0
        for num in perm:
            if num[0] != 0 and num[2] % 2 == 0:
                ans += 1
        
        return ans