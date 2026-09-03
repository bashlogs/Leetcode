class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        return sum(int(key) * val for key, val in Counter(str(n)).items())