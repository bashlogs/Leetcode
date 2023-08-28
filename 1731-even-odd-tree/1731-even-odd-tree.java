class Solution {
    public boolean isEvenOddTree(TreeNode root) {
        if(root == null) return true;
        Queue<TreeNode> q = new LinkedList<>();
        q.add(root);
        System.out.println(q.size());
        boolean evenlevel = true;
        while(q.size() > 0){
            int size = q.size();
            int prev = evenlevel ? Integer.MIN_VALUE : Integer.MAX_VALUE;
            while(size-- > 0){
                root = q.poll();
                if(evenlevel && (root.val % 2 == 0 || root.val <= prev)) return false;
                if(!evenlevel && (root.val % 2 == 1 || root.val >= prev)) return false;
                prev = root.val;
                if(root.left != null){
                    q.add(root.left);
                }
                if(root.right != null){
                    q.add(root.right);
                }
            }
            evenlevel = !evenlevel;
        }
        return true;
    }
}