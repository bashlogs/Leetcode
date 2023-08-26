/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public boolean check(TreeNode rootl, TreeNode rootr){
        if(rootl == null && rootr == null){
            return true;
        }
        if(rootl == null || rootr == null){
            return false;
        }
        if(rootl.val != rootr.val){
            return false;
        }

        return check(rootl.left, rootr.right) && check(rootl.right, rootr.left);
    }

    public boolean isSymmetric(TreeNode root) {
        if(root == null){
            return true;
        }
        return check(root.left, root.right);
    }
}