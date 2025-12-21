class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n,m = len(strs[0]),len(strs)
        is_correct = [False] * (m-1)
        res = 0
        for j in range(n):
            correct = True
            for i in range(m-1):
                if is_correct[i]:
                    continue
                elif strs[i][j] > strs[i+1][j]:
                    correct = False
                    break
            if not correct:
                res += 1
                continue
            for i in range(m-1):
                if not is_correct[i] and strs[i][j] < strs[i+1][j]:
                    is_correct[i] = True
                
        return res