class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        li = []
        st = ''
        for i in nums:
            st += str(i)
        for j in st:
            li.append(int(j))
        return li
        