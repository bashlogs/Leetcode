class Solution {
    public int lengthOfLastWord(String s) {
        int count = 0;
        int check = 0;
        for(int i=0; i<s.length(); i++){
            if(s.charAt(i) == ' '){
                check = 1;
            }
            else{
                if(check == 1){
                    count = 1;
                    check = 0;
                }
                else{
                    count++;
                }
            }
        }
        return count;
    }
}