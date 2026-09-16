# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: TreeNode | None) -> list[TreeNode | None]:
        
        dictionary = defaultdict(list)
        unique_set = set()
        unique_ans_set = set()
        ans = []

        def postorder(root):
            if root == None:
                return ["C"]
            
            left = postorder(root.left)
            right = postorder(root.right)

            comb = left + right + [root.val]

            if tuple(comb) in unique_set and tuple(comb) not in unique_ans_set:
                unique_ans_set.add(tuple(comb))
                ans.append(root)
            else:
                unique_set.add(tuple(comb))

            return comb
        
        postorder(root)

        return ans