class Solution {

    int height(TreeNode root) {
        if (root == null) {
            return 0;
        } else {
            int lheight = height(root.left);
            int rheight = height(root.right);
            return Math.max(lheight, rheight) + 1;
        }
    }

    void printlevel(TreeNode root, List<List<String>> l2, int level, int left, int right) {
        if (root == null) {
            return;
        }

        int mid = left + (right - left) / 2;
        l2.get(level).set(mid, Integer.toString(root.val));
        printlevel(root.left, l2, level+1, left, mid-1);
        printlevel(root.right, l2, level+1, mid+1, right);

        
    }

    public List<List<String>> printTree(TreeNode root) {
        int count = height(root);
        int spaces = (1 << count) - 1;

        List<List<String>> l1 = new ArrayList<>();
        for (int i = 0; i < count; i++) {
            List<String> l2 = new ArrayList<>();
            for(int j=0; j<spaces; j++){
                l2.add("");
            }
            l1.add(l2);
        }

        printlevel(root, l1, 0, 0, spaces-1);
        return l1;
    }
}
