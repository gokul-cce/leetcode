class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        curr_max = curr_min = 0
        maximum = minimum = 0
        total = 0
        for i in nums:
            curr_max = max(curr_max+i,i)
            curr_min = min(curr_min+i,i)
            maximum = max(maximum,curr_max)
            minimum = min(minimum,curr_min)
        total = max(total,maximum,abs(minimum))
        return total

        