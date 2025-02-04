class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        res = 0
        left = 0 
        right = 0
        total = 0
        while right < len(nums):
            if left == right:
                total = nums[left]
                res = max(res,total)
                right += 1
            elif nums[left] < nums[right]:
                total += nums[right]
                res = max(res,total)
                left += 1
                right += 1
            else:
                left = right
        return res

    




        