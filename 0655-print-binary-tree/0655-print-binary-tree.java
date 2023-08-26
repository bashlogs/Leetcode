class Solution {

    int getHeight(TreeNode root) {
        if (root == null) {
            return 0;
        }
        int leftHeight = getHeight(root.left);
        int rightHeight = getHeight(root.right);
        return Math.max(leftHeight, rightHeight) + 1;
    }

    void fillResult(TreeNode root, List<List<String>> result, int level, int left, int right) {
        if (root == null) {
            return;
        }
        
        int mid = left + (right - left) / 2;
        result.get(level).set(mid, Integer.toString(root.val));
        
        fillResult(root.left, result, level + 1, left, mid - 1);
        fillResult(root.right, result, level + 1, mid + 1, right);
    }

    public List<List<String>> printTree(TreeNode root) {
        int height = getHeight(root);
        int width = (1 << height) - 1; // Calculate the width of the resulting grid
        
        List<List<String>> result = new ArrayList<>();
        for (int i = 0; i < height; i++) {
            List<String> row = new ArrayList<>();
            for (int j = 0; j < width; j++) {
                row.add("");
            }
            result.add(row);
        }
        
        fillResult(root, result, 0, 0, width - 1);
        return result;
    }
}
