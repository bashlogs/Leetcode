class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        graph1 = defaultdict(list)
        ans = []
        safe = set()
        queue = deque()

        for i, node in enumerate(graph):
            if not node:
                safe.add(i)
                queue.append(i)
                continue

            for n in node:
                graph1[n].append(i)

        while queue:
            node = queue.popleft()

            for parent in graph1[node]:
                if all(child in safe for child in graph[parent]):
                    if parent not in safe:
                        safe.add(parent)
                        queue.append(parent)

        return sorted(safe)