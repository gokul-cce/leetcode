class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1]
        for i in range(len(nums)-1):
            prefix.append(prefix[-1]*nums[i])
        suffix = [1]
        for i in range(len(nums)-1,0,-1):
            suffix.append(suffix[-1]*nums[i])
        suffix = suffix[::-1]
        result = []
        for i in range(len(nums)):
            result.append(prefix[i]*suffix[i])
        return result

        