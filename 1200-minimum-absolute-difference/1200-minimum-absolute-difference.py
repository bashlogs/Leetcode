class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        freq = defaultdict(list)

        for i in range(len(arr) - 1):
            temp = abs(arr[i] - arr[i+1])
            freq[temp].append((arr[i], arr[i+1]))
        
        ans = float('inf')

        for k, v in freq.items():
            ans = min(ans, k)
        
        return freq[ans]