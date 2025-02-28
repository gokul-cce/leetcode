class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = 0
        right = len(nums)-1
        index1 = -1
        while left <= right:
            middle = (left + right) // 2
            if nums[middle] == target:
                index1 = middle
            if nums[middle] < target:
                left = middle + 1
            else:
                right = middle - 1
        if index1 == -1:
            return [-1,-1]
        left = 0
        right = len(nums)-1
        index2 = -1
        while left <= right:
            middle = (left+right)//2
            if nums[middle] == target:
                index2 = middle
            if nums[middle] <= target:
                left = middle + 1
            else:
                right = middle - 1
        return [index1,index2]