class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse=True)
        curr = 0
        ans = 0

        for i in happiness:
            if i - curr < 0 or k - curr <= 0:
                break
            
            ans += (i - curr)
            curr += 1

        return ans