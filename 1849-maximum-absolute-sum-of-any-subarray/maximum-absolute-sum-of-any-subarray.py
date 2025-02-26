class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        prefix = [nums[0]]
        for i in nums:
            prefix.append(prefix[-1]+i)
        return max(prefix)-min(prefix)