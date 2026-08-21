class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(list)

        for i, j, k in roads:
            graph[i].append([j,k])
            graph[j].append([i,k])
        
        visited = set()
        queue = deque([1])
        min_val = float('inf')

        while queue:
            curr = queue.popleft()
            visited.add(curr)

            for u, val in graph[curr]:
                if u not in visited:
                    min_val = min(min_val, val)
                    queue.append(u)
            
        return min_val
                

