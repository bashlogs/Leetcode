class Solution {
    boolean checkgrid(int row, int col, int[][] grid){
        boolean[] tre = new boolean[10];
        Arrays.fill(tre, false);
        for(int i=row; i<row + 3; i++){
            for(int j=col; j< col + 3; j++){
                int num = grid[i][j];
                if(num < 1 || num > 9) return false;
                if(tre[num]) return false;
                tre[num] = true;
            }
        }

        int left = grid[row][col] + grid[row+1][col+1] + grid[row+2][col+2];
        int right = grid[row+2][col] + grid[row+1][col+1] + grid[row][col+2];

        if(left != right){
            return false;
        }

        for(int i=row; i<row+3; i++){
            int cal = 0;
            for(int j=col; j<col+3; j++){
                cal += grid[i][j];
            }
            if(cal != left){
                return false;
            }
            else{
                cal = 0;
            }
        }

        for(int j=col; j<col+3; j++){
            int cal = 0;
            for(int i=row; i<row+3; i++){
                cal += grid[i][j];
            }
            if(cal != right){
                return false;
            }
            else{
                cal = 0;
            }
        }

        return true;
    }

    public int numMagicSquaresInside(int[][] grid) {
        if(grid.length < 3){
            return 0;
        }

        int count = 0;
        for(int i=0; i<grid.length - 2; i++){
            for(int j=0; j<grid[0].length - 2; j++){
                if(checkgrid(i,j,grid)){
                    count++;
                }
            }
        }

        return count;
    }
}