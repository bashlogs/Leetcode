class Solution:
    def judgeCircle(self, moves: str) -> bool:
        pos = [0, 0]

        for i in moves:
            if i == 'R':
                pos[1] += 1
            elif i == 'L':
                pos[1] -= 1
            elif i == 'D':
                pos[0] += 1
            else:
                pos[0] -= 1
        
        return pos == [0, 0]