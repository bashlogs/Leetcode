class Solution {
    public int lengthOfLastWord(String s) {
        int len = s.length()-1;
        int size = 0;
        while(s.charAt(len) == ' '){
            len--;
        }
        while(len>=0 && s.charAt(len) != ' '){
            size++;
            len--;
        }
        return size;
    }
}