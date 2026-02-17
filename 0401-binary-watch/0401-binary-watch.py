class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        times = []
        for h in range(12):
            for m in range(60):
                hones = bin(h).count('1')
                mones = bin(m).count('1')

                if hones + mones == turnedOn:
                    times.append(f"{h}:{m:02d}")
        
        return times