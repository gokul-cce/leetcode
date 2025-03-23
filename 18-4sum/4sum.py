class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        n = len(nums)
        for i in range(n):
            for j in range(i+1,n):
                hashset = set()
                for k in range(j+1,n):
                    total = nums[i]+nums[j]+nums[k]
                    fourth = target - total
                    if fourth in hashset:
                        temp = [nums[i],nums[j],nums[k],fourth]
                        temp.sort()
                        if temp not in ans:
                            ans.append(temp)
                    hashset.add(nums[k])
        return ans
            



        