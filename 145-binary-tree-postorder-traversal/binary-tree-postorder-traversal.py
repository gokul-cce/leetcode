# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def helper(root,pos):
            if root is None:
                return None
            helper(root.left,pos)
            helper(root.right,pos)
            pos.append(root.val)
            return pos

        pos = []
        return helper(root,pos)
        