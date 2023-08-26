class Solution {
    TreeNode check(int[] nums, int start, int end){
        if(start > end){
            return null;
        }

        int pos = start;
        for(int i=start+1; i<=end; i++){
            if(nums[i] > nums[pos]){
                pos = i;
            }
        }

        return new TreeNode(nums[pos], check(nums, start, pos-1), check(nums, pos+1, end));
    }

    public TreeNode constructMaximumBinaryTree(int[] nums) {
        return check(nums, 0, nums.length - 1);
    }
}