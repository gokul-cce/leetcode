class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        single = 0
        double = 0
        for i in nums:
            if i < 10:
                single += i
            else:
                double += i
        if single > double or double > single:
            return True
        return False
        