class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        x_building = sorted(buildings, key = lambda x: (x[1], x[0]))
        y_building = sorted(x_building, key = lambda x: (x[0], x[1]))

        map1 = defaultdict(int)
        count = 0

        for i in range(1, len(x_building) - 1):
            if x_building[i-1][1] == x_building[i][1]:
                map1[tuple(x_building[i])] += 1
            
            if x_building[i][1] == x_building[i+1][1]:
                map1[tuple(x_building[i])] += 1
            
            if y_building[i-1][0] == y_building[i][0]:
                map1[tuple(y_building[i])] += 1
            
            if y_building[i][0] == y_building[i+1][0]:
                map1[tuple(y_building[i])] += 1
        
        for k, v in map1.items():
            if v >= 4:
                count += 1

        return count