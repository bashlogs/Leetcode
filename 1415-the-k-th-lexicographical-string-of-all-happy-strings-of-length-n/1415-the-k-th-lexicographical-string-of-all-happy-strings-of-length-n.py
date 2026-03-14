class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        comb = []
        words = ["a", "b", "c"]

        def generate(word, left):
            if len(comb) >= k:
                return 

            if left == 0:
                comb.append(word)
                return

            for i in words:
                if i != word[-1]:
                    generate(word + i, left - 1)

        for i in words:
            generate(i, n - 1)
        
        return comb[k-1] if len(comb) >= k else ""