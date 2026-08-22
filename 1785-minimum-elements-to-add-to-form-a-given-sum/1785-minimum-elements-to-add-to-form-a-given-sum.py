class Solution:
    def minElements(self, nums: List[int], limit: int, goal: int) -> int:
        total = sum(nums)
        need = abs(goal - total)
        div = need//limit
        rem = need%limit

        if rem:
            return div + 1
        else:
            return div