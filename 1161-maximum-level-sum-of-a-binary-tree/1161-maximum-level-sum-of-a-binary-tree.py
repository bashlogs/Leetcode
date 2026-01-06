# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        level = 1
        maximum = root.val

        queue = deque([root])
        curr = 1

        while queue:
            size = len(queue)
            total = 0

            for i in range(size):
                temp = queue.popleft()
                total += temp.val
                
                if temp.left != None:
                    queue.append(temp.left)
                
                if temp.right != None:
                    queue.append(temp.right)
            
            if total > maximum:
                maximum = total
                level = curr

            curr += 1
        
        return level