class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        
        colored_house = {}
        ans = 0

        for i in range(len(colors)):
            for k, v in colored_house.items():
                if k != colors[i]:
                    ans = max(ans, i - v)
            
            if colors[i] not in colored_house:
                colored_house[colors[i]] = i
        
        return ans