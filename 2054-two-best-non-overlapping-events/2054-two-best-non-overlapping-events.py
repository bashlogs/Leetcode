class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        attend = []
        events.sort(key = lambda x: x[0])

        max_val = 0
        max_sum = 0

        for event in events:
            while attend and attend[0][0] < event[0]:
                max_val = max(max_val, attend[0][1])
                heapq.heappop(attend)
            
            max_sum = max(max_sum, max_val + event[2])

            heapq.heappush(attend, (event[1], event[2]))
        
        return max_sum