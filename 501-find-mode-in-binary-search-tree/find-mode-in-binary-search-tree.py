# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(root):
            if root == None:
                return 
                
            counter[root.val] += 1
            dfs(root.left)
            dfs(root.right)

        counter = defaultdict(int)
        dfs(root)
        max_freq = max(counter.values())

        ans = []
        for k, v in counter.items():
            if v == max_freq:
                ans.append(k)
        
        return ans