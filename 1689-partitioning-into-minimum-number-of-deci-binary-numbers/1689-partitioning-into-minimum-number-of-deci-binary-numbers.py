class Solution:
    def minPartitions(self, n: str) -> int:
        """

        82734
        .

        11111 - 71623
        11111 - 60512
        10111 - 50402
        10101 - 40301
        10101 - 30200
        10100 - 20100
        10100 - 10000
        10000

        """
        max = 0
        for i in range(len(n)):
            if int(n[i]) > max:
                max = int(n[i])
        
        return max