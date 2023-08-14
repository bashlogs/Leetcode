class Solution {
    public int minimumLength(String s) {
        int a = 0;
        int j = s.length()-1;

        while(a < j){
            if(s.charAt(a) == s.charAt(j)){
                a++;
                j--;
                while(a<=j && s.charAt(a) == s.charAt(a-1)){
                    a++;
                }
                while(a<=j && s.charAt(j) == s.charAt(j+1)){
                    j--;
                }
            }
            else{
                break;
            }
        }

        
        System.out.println(a+" "+j);
        if(a == j){
            return 1;
        }
        else if(a > j){
            return 0;
        }
        else{
            String new1 = new String();
            for(int i=a; i<=j; i++){
                new1 += s.charAt(a);
            }
            return new1.length();
        }
    }
}