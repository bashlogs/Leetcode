# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def getMin(self, root):
        while (root.left != None):
            root = root.left
        
        return root

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        
        if (root != None):
            if (root.val < key):
                root.right = self.deleteNode(root.right, key)
            elif (root.val > key):
                root.left = self.deleteNode(root.left, key)
            else:
                if (root.left == None and root.right == None):
                    return None
                elif (root.left != None and root.right == None):
                    return root.left
                elif (root.right != None and root.left == None):
                    return root.right
                else:
                    temp = self.getMin(root.right)
                    root.val = temp.val
                    root.right = self.deleteNode(root.right, temp.val)
        
        return root
