# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        
        def height(root):
            if root == None:
                return 0
            
            left = height(root.left)
            right = height(root.right)

            return max(left, right) + 1
        
        def preorder(root, level):
            if root == None:
                return

            arr[level] += root.val

            preorder(root.left, level + 1)
            preorder(root.right, level + 1)
        

        arr = [0] * (height(root) + 1)
        preorder(root, 1)

        maxval = arr[1]
        level = 1

        for i in range(2, len(arr)):
            if arr[i] > maxval:
                maxval = arr[i]
                level = i
        
        return level