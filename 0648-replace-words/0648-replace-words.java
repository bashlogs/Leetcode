class Solution {
    public String replaceWords(List<String> dictionary, String sentence) {
        Collections.sort(dictionary, Comparator.comparingInt(String::length));
        String[] str = sentence.split(" ");
        for(int i=0; i<str.length; i++){
            for(int j=0; j<dictionary.size(); j++){
                if(str[i].startsWith(dictionary.get(j))){
                    str[i] = dictionary.get(j);
                    break;
                }
            }
        }
        String ans = String.join(" ", str);
        return ans;
    }
}