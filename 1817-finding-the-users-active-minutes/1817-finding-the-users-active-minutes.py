class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        hashmap = defaultdict(set)
        ans = [0] * k
        for id, time in logs:
            hashmap[id].add(time)
        
        for k, v in hashmap.items():
            ans[len(v) - 1] += 1
        
        return ans