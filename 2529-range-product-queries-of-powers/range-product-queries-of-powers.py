class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        binary_val = bin(n)[2:]
        arr = []
        prev = 1
        val = 1
        mod = 10**9 + 7

        ans = []

        for i in range(len(binary_val) - 1, -1, -1):
            if binary_val[i] == '1':
                temp = prev * val
                arr.append(temp)
                prev = temp

            val += val
        
        for query in queries:
            if query[0] == 0:
                ans.append((arr[query[1]]) % mod)
            else:
                ans.append((arr[query[1]] // arr[query[0] - 1]) % mod)

        return ans
            
