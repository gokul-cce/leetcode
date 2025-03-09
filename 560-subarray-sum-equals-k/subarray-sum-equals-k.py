class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        dic = {0:1}
        result = 0
        prefix = 0
        for i in range(len(nums)):
            prefix += nums[i]
            remain = prefix - k
            if remain in dic:
                result += dic[remain]
                # dic[remain] += 1
            if prefix in dic:
                dic[prefix] += 1
            else:
                dic[prefix] = 1
            # print(dic)
        return result
        
        