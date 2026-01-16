class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        hashmap = defaultdict(set)
        ans = [0] * k
        
        for id, time in logs:
            if time not in hashmap[id]:
                if len(hashmap[id]) > 0:
                    ans[len(hashmap[id]) - 1] -= 1

                hashmap[id].add(time)
                ans[len(hashmap[id]) - 1] += 1
        
        return ans