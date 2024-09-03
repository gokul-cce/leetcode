class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s) > k:
            st = ''
            total = 0
            for i in range(len(s)):
                if i % k == k - 1:
                    total += int(s[i])
                    st += str(total)
                    total = 0
                else:
                    total += int(s[i])
            if len(s) % k != 0:
                st += str(total)
            s = st
        return s
        