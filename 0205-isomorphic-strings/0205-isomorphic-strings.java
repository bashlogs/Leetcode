class Solution {
    public boolean isIsomorphic(String s, String t) {
        if(s.length()!=t.length())return false;
        
        Map<Character, Character> data = new HashMap<>();
        for(int i=0; i<s.length(); i++){
            if(data.containsKey(s.charAt(i)) && data.get(s.charAt(i)) != t.charAt(i)){
                return false;
            }
            else if(!data.containsKey(s.charAt(i)) && data.containsValue(t.charAt(i))){
                return false;
            }
            else{
                data.put(s.charAt(i), t.charAt(i));
            }
        }

        return true;
    }
}