class Solution {
    public int[] countBits(int n) {
        int sol[]=new int[n+1];
        sol[0]=0;
        for(int i=1;i<=n;i++){
            sol[i]=numOnes(i);
        }
        return sol;
    }
    private int numOnes(int n){
        int count=0;
        while(n!=0){
            count+=(n&1);
            n>>>=1;
        }
        return count;
    }
}