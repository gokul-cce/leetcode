# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def helper(nums,left,right):
            if left > right:
                return None
            middle = (left + right) // 2
            element = TreeNode(nums[middle])
            element.left = helper(nums,left,middle-1)
            element.right = helper(nums,middle+1,right)
            return element
        return helper(nums,0,len(nums)-1)

        