class Solution {
    public String convertToTitle(int columnNumber) {
        StringBuilder output = new StringBuilder();
        while(columnNumber > 0){
            int rem = columnNumber%26;
            if(rem == 0){
                output.insert(0,'Z');
                columnNumber = (columnNumber/26)-1;
            }
            else{
                output.insert(0, (char) (rem-1+'A'));
                columnNumber = columnNumber/26;
            }
        }
        return output.toString();
    }
}