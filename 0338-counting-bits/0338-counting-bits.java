class Solution {
    public int count(String num){
        int count = 0;
        for(int i=0;i<num.length(); i++){
            if(num.charAt(i) == '1'){
                count++;
            }
        }
        return count;
    }
    public int[] countBits(int n) {
        int[] count = new int[n+1];
        for(int i=0; i<=n; i++){
            count[i] = count(Integer.toBinaryString(i));
        }
        return count;
    }
}