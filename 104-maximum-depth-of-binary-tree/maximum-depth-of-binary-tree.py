# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        count = 0
        temp = root
        def length(temp,count):
            if temp:
                count += 1
                l = length(temp.left,count)
                r = length(temp.right,count)
                count = max(l,r)
            return count
        return length(temp,count)
            
        