class Solution:
    def minElements(self, nums: List[int], limit: int, goal: int) -> int:
        total = sum(nums)
        need = abs(goal - total)
        div = need//limit
        rem = need%limit
        return div + 1 if rem else div