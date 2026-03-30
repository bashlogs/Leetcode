class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        even_set_s1 = defaultdict(int)
        odd_set_s1 = defaultdict(int)

        even_set_s2 = defaultdict(int)
        odd_set_s2 = defaultdict(int)

        for i in range(len(s1)):
            if i % 2 == 0:
                even_set_s1[s1[i]] += 1
                even_set_s2[s2[i]] += 1
            else:
                odd_set_s1[s1[i]] += 1
                odd_set_s2[s2[i]] += 1
        
        if even_set_s1 == even_set_s2 and odd_set_s1 == odd_set_s2:
            return True
        else:
            return False