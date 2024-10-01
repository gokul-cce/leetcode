class Solution:
    def climbStairs(self, n: int) -> int:
        dup = [0]*(n+1)
        def stairs(n,dup):
            if 0 <= n <= 1:
                return 1
            if dup[n] != 0:
                return dup[n]
            dup[n] = stairs(n-1,dup) + stairs(n-2,dup)
            return dup[n]
        return stairs(n,dup)
        