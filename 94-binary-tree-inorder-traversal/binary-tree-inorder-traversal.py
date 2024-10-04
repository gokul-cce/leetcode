# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def inorder(root,res):
            if root is None:
                return None
            left = inorder(root.left,res)
            res.append(root.val)
            right = inorder(root.right,res)
            return res

        return inorder(root,res)
        