class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        li = []
        for i in nums:
            for j in str(i):
                li.append(int(j))
        return li
        