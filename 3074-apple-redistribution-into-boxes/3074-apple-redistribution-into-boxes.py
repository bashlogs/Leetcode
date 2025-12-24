class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        total = sum(apple)

        capacity.sort(reverse=True)
        i = 0
        while total > 0 and i < len(capacity):
            total -= capacity[i]
            i += 1
        
        if total > 0:
            return -1
        else:
            return i
        
