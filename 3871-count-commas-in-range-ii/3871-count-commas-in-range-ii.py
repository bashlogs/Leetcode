class Solution:
    def countCommas(self, n: int) -> int:
        def comma_count(num):
            comma = (len(num) - 1) // 3
            if comma > 0:
                neg = '999' * comma
                temp = (int(num) - int(neg)) * comma

                return temp + comma_count(neg)

            else:
                return 0

        return comma_count(str(n))