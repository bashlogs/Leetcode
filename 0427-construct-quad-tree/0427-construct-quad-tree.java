class Solution {
    boolean isgrid(int[][] grid, int top, int left, int bottom, int right){
        int key = grid[top][left];
        for(int i=top; i<bottom; i++){
            for(int j=left; j<right; j++){
                if(grid[i][j] != key){
                    return false;
                }
            }
        }
        return true;
    }


    public Node construct1(int[][] grid, int top, int left, int bottom, int right){
        if(isgrid(grid, top, left, bottom, right)){
            return new Node(grid[top][left] == 1, true);
        }

        int mid_row = (top + bottom) / 2;
        int mid_col = (left + right) / 2;

        Node node = new Node(true, false);
        node.topLeft = construct1(grid, top, left, mid_row, mid_col);
        node.topRight = construct1(grid, top, mid_col, mid_row, right);
        node.bottomLeft = construct1(grid, mid_row, left, bottom, mid_col);
        node.bottomRight = construct1(grid, mid_row, mid_col, bottom, right);

        return node;
    }

    public Node construct(int[][] grid) {
        int len = grid.length;
        return construct1(grid, 0, 0, len, len);
    }
}