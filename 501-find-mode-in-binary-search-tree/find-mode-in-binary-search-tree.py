# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        max_freq = 0
        counter = defaultdict(int)

        def dfs(root):
            nonlocal max_freq
            if root == None:
                return 

            counter[root.val] += 1
            if counter[root.val] > max_freq:
                max_freq = counter[root.val]

            dfs(root.left)
            dfs(root.right)

        dfs(root)

        ans = []
        for k in counter:
            if counter[k] == max_freq:
                ans.append(k)
        
        return ans