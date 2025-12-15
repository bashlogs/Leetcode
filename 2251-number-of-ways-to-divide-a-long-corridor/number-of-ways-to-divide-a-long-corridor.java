class Solution {
    static final int MOD = 1000_000_007;

    public int solve(int i, String corridor, int n, int seats, int dp[][]) {
        if (i >= n)
            return seats == 2 ? 1 : 0;
        if (dp[seats][i] != -1)
            return dp[seats][i];
        char c = corridor.charAt(i);
        if (c == 'S') {
            if (seats == 2)
                return dp[seats][i] = solve(i + 1, corridor, n, 1, dp) % MOD;
            return dp[seats][i] = solve(i + 1, corridor, n, seats + 1, dp) % MOD;
        } else {
            if (seats == 2)
                return dp[seats][i] = ((solve(i + 1, corridor, n, seats, dp) % MOD)
                        + (solve(i + 1, corridor, n, 0, dp) % MOD)) % MOD;
            return dp[seats][i] = solve(i + 1, corridor, n, seats, dp) % MOD;
        }
    }

    public int numberOfWays(String corridor) {
        int n = corridor.length();
        int dp[][] = new int[3][n];
        for (int i[] : dp)
            Arrays.fill(i, -1);
        return solve(0, corridor, corridor.length(), 0, dp);
    }
}