class Solution:
    def alternateDigitSum(self, n: int) -> int:
        total = 0
        st = str(n)
        for i in range(len(st)):
            if i % 2:
                total -= int(st[i])
            else:
                total += int(st[i])
        return total

        