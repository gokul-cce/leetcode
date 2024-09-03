class Solution:
    def alternateDigitSum(self, n: int) -> int:
        total = 0
        flag = 1
        for i in str(n):
            total += (flag * int(i))
            flag *= -1
        return total

        