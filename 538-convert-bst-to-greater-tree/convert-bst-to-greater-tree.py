# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        last_num = 0

        def rec(root):
            nonlocal last_num
            if root == None:
                return

            rec(root.right)
            root.val = root.val + last_num
            last_num = root.val
            rec(root.left)
        
        rec(root)

        return root

