class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        single = double = 0
        for i in nums:
            if i < 10:
                single += i
            else:
                double += i
    
        return single != double
        