class Solution:
    def longestBalanced(self, s: str) -> int:
        """



        """

        ans = 0
        ch_count = defaultdict(int)
        nu_count = defaultdict(set)

        for i in range(len(s)):
            # print(i)
            for j in range(i, len(s)):
                # Remove
                if s[j] in ch_count:
                    prev = ch_count[s[j]]
                    nu_count[prev].remove(s[j])
                    
                    if len(nu_count[prev]) == 0:
                        del nu_count[prev]

                ch_count[s[j]] += 1
                nu_count[ch_count[s[j]]].add(s[j])

                if len(nu_count) == 1:
                    for k, v in nu_count.items():
                        ans = max(ans, k * len(v))

                # print(ch_count, nu_count)

            ch_count.clear()
            nu_count.clear()
        
        return ans

