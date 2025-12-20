class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        
        n = len(strs[0])
        m = len(strs)

        count = 0

        for j in range(n):
            for i in range(1, m):
                if strs[i-1][j] > strs[i][j]:
                    count += 1
                    break
        
        return count

