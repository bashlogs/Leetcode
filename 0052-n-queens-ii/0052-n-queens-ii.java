class Solution {
    private int sol = 0;

    boolean isSafe(int row, int col, int[][] board, int n){
        for (int i = col; i >= 0; i--) {
            if (board[row][i] == 1) {
                return false;
            }
        }

        int i = row, j = col;
        while (i >= 0 && j >= 0) {
            if (board[i--][j--] == 1) {
                return false;
            }
        }

        i = row;
        j = col;
        while (i < n && j >= 0) {
            if (board[i++][j--] == 1) {
                return false;
            }
        }

        return true;
    }
    void placeQueen(int n, int[][] board, int pos){
        if(pos >= n){
            return;
        }

        for (int i = 0; i < n; i++) {
            if (isSafe(i, pos, board, n)) {
                board[i][pos] = 1;
                if (pos == n - 1) {
                    sol++;
                }
                placeQueen(n, board, pos + 1);
                board[i][pos] = 0;
            }
        }
    }
    public int totalNQueens(int n) {
        if(n == 1){
            return 1;
        }
        int chessBoard[][] = new int[n][n];
        for (int i = 0; i < n; i++) {
            Arrays.fill(chessBoard[i], 0);
        }
        placeQueen(n, chessBoard, 0);
        return sol;
    }
}