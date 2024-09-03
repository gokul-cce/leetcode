class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        element = digit = 0
        st = ''
        for i in nums:
            element += i
            st += str(i)
        for j in st:
            digit += int(j)
        st = element - digit
        if st < 0:
            return st * (-1)
        return st

        