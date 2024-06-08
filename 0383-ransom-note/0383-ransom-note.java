class Solution {
    public boolean canConstruct(String ransomNote, String magazine) {
        Map<Character, Integer> data = new HashMap<>();

        for(int i=0; i<magazine.length(); i++){
            data.put(magazine.charAt(i), data.getOrDefault(magazine.charAt(i), 0) + 1);
        }

        for(int i=0; i<ransomNote.length(); i++){
            if(data.containsKey(ransomNote.charAt(i)) && data.get(ransomNote.charAt(i)) >= 1){
                data.put(ransomNote.charAt(i), data.get(ransomNote.charAt(i)) - 1);
            }
            else{
                return false;
            }
        }

        return true;
    }
}