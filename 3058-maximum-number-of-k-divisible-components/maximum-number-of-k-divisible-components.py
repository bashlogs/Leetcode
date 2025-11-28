class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        adj_list = [[] for _ in range(n)]
        for n1, n2 in edges:
            adj_list[n1].append(n2)
            adj_list[n2].append(n1)
        
        component_count = [0]

        def dfs(curr, parent, adj, node_value, k, count):
            sum_ = 0

            for nei in adj[curr]:
                if nei != parent:
                    sum_ += dfs(nei, curr, adj, node_value, k, count)
                    sum_ %= k
            
            sum_ += node_value[curr]
            sum_ %= k

            if sum_ == 0:
                count[0] += 1
            
            return sum_

        dfs(0, -1, adj_list, values, k, component_count)

        return component_count[0]
    
