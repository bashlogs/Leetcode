class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        val = 1 << k
        freq = set()
        for i in range(len(s) - (k-1)):
            freq.add(s[i:i+k])
        
        for i in range(val):
            num = bin(i)[2:]
            if f"{int(num):0{k}d}" not in freq:
                return False
        
        return True