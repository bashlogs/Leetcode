class Solution {
    public int romanToInt(String s) {
        Map<Character, Integer> data = new HashMap<>();
        data.put('I', 1);
        data.put('V', 5);
        data.put('X', 10);
        data.put('L', 50);
        data.put('C', 100);
        data.put('D', 500);
        data.put('M', 1000);

        int ans = 0;
        for(int i=0; i<s.length(); i++){
            if(i < s.length() - 1 && data.get(s.charAt(i)) < data.get(s.charAt(i+1))){
                ans -= data.get(s.charAt(i));
            }
            else{
                ans += data.get(s.charAt(i));
            }
        }

        return ans;
        

    }
}