class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        dic = {}
        for i in range(len(nums)):
            rem = target - nums[i]
            if rem in dic:
                return [dic[rem],i]
            dic[nums[i]] = i 
        
        # for i in range(len(nums)):
        #     dic[nums[i]] = i
        # print(dic)
        # for j in range(len(nums)):
        #     compliment = target - nums[j]
        #     if compliment in dic and dic[compliment] != j:
        #         return [j,dic[compliment]]

        
        # for i in range(len(nums)):
        #     compliment = target - nums[i]
        #     if compliment in dic:
        #         return [dic[compliment],i]

        #     dic[nums[i]] = i
        
        