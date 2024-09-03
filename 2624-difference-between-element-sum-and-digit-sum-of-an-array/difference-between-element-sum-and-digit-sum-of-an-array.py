class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        element = sum(nums)
        for j in nums:
            while j > 0:
                element = element - (j % 10)
                j = j // 10

        if element < 0:
            return element * (-1)
        return element

        