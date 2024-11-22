# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        depth = 0
        def helper(root,depth):
            if not root:
                return 0
            # depth += 1
            if root.left and root.right:
                left = helper(root.left,depth)
                right = helper(root.right,depth)
                return 1 + min(left,right)
            elif root.right:
                right = helper(root.right,depth)
                return 1 + right
            elif root.left:
                left = helper(root.left,depth)
                return 1 + left
            else:
                return 1
        return helper(root,depth)
        