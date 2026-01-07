class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        ans = 0
        mod = 10**9 + 7
        def traverse(root):
            if root == None:
                return 0
            
            left = traverse(root.left)
            right = traverse(root.right)

            root.val += (left + right)
            return root.val
        
        def traverse2(root, total):
            nonlocal ans

            if root.left == None and root.right == None:
                return
            
            if root.left:
                ans = max(ans, ((total - root.left.val) * root.left.val))
                traverse2(root.left, total)

            if root.right:
                ans = max(ans, ((total - root.right.val) * root.right.val))
                traverse2(root.right, total)

        traverse(root)
        
        traverse2(root, root.val)
        
        return ans % mod