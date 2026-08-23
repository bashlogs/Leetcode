class Solution:
    def sumGame(self, nums: str) -> bool:
        empty1, empty2 = 0, 0
        arr1, arr2 = 0, 0

        for i in range(len(nums)//2):
            if nums[i] == '?':
                empty1 += 1
            else:
                arr1 += int(nums[i])
        
        for i in range(len(nums)//2, len(nums)):
            if nums[i] == '?':
                empty2 += 1
            else:
                arr2 += int(nums[i])

        if (empty1 + empty2) % 2 == 1:
            return True 

        diff = arr1 - arr2

        if diff == 9 * (empty2 - empty1) // 2:
            return False
        
        return True

        
            




