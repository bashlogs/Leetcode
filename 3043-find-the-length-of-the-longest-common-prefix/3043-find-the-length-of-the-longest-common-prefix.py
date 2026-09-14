class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        set_arr = set()
        final_ans = 0
        
        for num in arr1:
            n = str(num)

            for i in range(1, len(n) + 1):
                set_arr.add(int(n[:i]))
        
        # print(set_arr)

        for num in arr2:
            n = str(num)
            ans = 0

            for i in range(1, len(n) + 1):
                if int(n[:i]) in set_arr:
                    ans += 1
                else:
                    break
            
            final_ans = max(ans, final_ans)
            
        return final_ans