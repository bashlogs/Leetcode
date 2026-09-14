# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        ans = 0

        def postorder(root):
            nonlocal ans
            if root is None:
                return (0, 0)
            
            left_val = postorder(root.left)
            right_val = postorder(root.right)

            val = left_val[0] + right_val[0] + root.val
            count = left_val[1] + right_val[1] + 1

            if val // count == root.val:
                ans += 1

            return (val, count)
        
        postorder(root)

        return ans
