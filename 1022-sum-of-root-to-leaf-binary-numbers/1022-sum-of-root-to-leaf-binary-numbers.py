# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        
        total = 0

        def rec(root, val):
            nonlocal total
            if root.left == None and root.right == None:
                total += int(val, 2)
                return

            
            if root.left != None:
                new_val = val + str(root.left.val)
                rec(root.left, new_val)
            
            if root.right != None:
                new_val = val + str(root.right.val)
                rec(root.right, new_val)

        rec(root, f"{root.val}")
        return total
            
