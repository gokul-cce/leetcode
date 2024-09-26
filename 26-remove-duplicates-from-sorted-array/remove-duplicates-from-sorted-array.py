class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        dup = []
        index = 0
        for i in range(len(nums)):
            if nums[i] not in dup:
                dup.append(nums[i])
                nums[i],nums[index] = nums[index],nums[i]
                index += 1
            else:
                continue
        
        return index

        