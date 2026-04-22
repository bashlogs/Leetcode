class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        ans = []
        
        for word in queries:
            for word2 in dictionary:
                count = 2
                i = 0

                while i < len(word2) and count >= 0 and count + i < len(word2):
                    if word[i] != word2[i]:
                        count -= 1
                    
                    i += 1
                
                if count >= 0:
                    ans.append(word)
                    break

        return ans