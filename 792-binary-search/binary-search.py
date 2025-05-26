class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def searching(nums,target,left,right):
            if left > right:
                return 
            middle = (left + right)//2
            if nums[middle] == target:
                return middle
            elif nums[middle] < target:
                return searching(nums,target,middle+1,right)
            else:
                return searching(nums,target,left,middle-1)


        res = searching(nums,target,0,len(nums)-1)
        if res != None:
            return res
        else:
            return -1



        