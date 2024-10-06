# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        res = []
        temp = root
        while stack or temp:
            if temp:
                stack.append(temp)
                temp = temp.left
            else:
                current = stack.pop()
                res.append(current.val)
                temp = current.right
        return res

        