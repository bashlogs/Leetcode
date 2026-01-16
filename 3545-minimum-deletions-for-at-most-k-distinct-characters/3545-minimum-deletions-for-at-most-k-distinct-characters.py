class Solution:
    def minDeletion(self, s: str, k: int) -> int:
        hashmap = defaultdict(int)

        for i in s:
            hashmap[i] += 1
        
        li = [[k, v] for k, v in hashmap.items()]

        li.sort(key = lambda x: (x[1]))

        i = 0
        total = 0

        while len(li) - i > k:
            total += li[i][1]
            i += 1
        
        return total
