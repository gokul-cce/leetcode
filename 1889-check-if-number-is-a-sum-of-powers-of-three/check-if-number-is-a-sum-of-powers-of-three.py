class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        power = int(n**(1/3))
        while n > 0 and power > -1:
            if n >= 3**power:
                n -= 3**power
            power -= 1
        return n==0
        