class Solution:
    def bestClosingTime(self, customers: str) -> int:
        max_score = 0
        ans = -1
        curr = 0
        for i, ch in enumerate(customers):
            if ch == 'Y':
                curr += 1
            else:
                curr -= 1
            
            if curr > max_score:
                ans = i
                max_score = curr
        
        return ans + 1