class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        expected = []
        for i in nums:
            if i != val:
                expected.append(i)
        n = len(expected)
        for j in range(n):
            nums[j] = expected[j]
        return n