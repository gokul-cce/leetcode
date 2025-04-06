class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maximum = nums[0]
        minimum = nums[0]
        res = nums[0]
        for i in range(1,len(nums)):
            if nums[i] < 0:
                maximum,minimum = minimum,maximum
            maximum = max(nums[i],nums[i]*maximum)
            minimum = min(nums[i],nums[i]*minimum)
            res = max(res,maximum)
        return res
        