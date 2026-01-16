class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        hashmap = defaultdict(set)
        ans = [0] * k
        
        for id, time in logs:
            if time not in hashmap[id]:
                l = len(hashmap[id])
                
                if l > 0:
                    ans[l - 1] -= 1

                if time not in hashmap[id]:
                    ans[l] += 1
                    hashmap[id].add(time)

        return ans