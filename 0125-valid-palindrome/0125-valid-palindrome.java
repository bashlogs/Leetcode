class Solution {
    public boolean isPalindrome(String s) {
        String n = s.replaceAll("[^A-Za-z0-9]", "").toLowerCase();
        
        int a = 0;
        int b = n.length()-1;
        while(a <= b){
            if(n.charAt(a) != n.charAt(b)){
                return false;
            }
            a++;
            b--;
            System.out.println(a+" "+b);
        }        
        return true;
    }
}