class Solution:
    def maxBalancedShipments(self, weight: List[int]) -> int:
        

        count = 0
        maximum = None

        for i in range(len(weight)):
            if maximum != None and weight[i] < maximum:
                count += 1
                maximum = None
            else:
                maximum = weight[i]
        
        return count