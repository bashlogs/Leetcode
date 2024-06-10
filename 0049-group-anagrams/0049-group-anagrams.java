import java.util.Map.*;

class Solution {
    public String sortString(String s){
        char ch[] = s.toCharArray();
        Arrays.sort(ch);
        return new String(ch);
    }

    public List<List<String>> groupAnagrams(String[] strs) {
        // List<String> index = new ArrayList<>();
        // int flag = 0;
        // Map<String, Integer> anagram = new HashMap<>();
        // List<String> data = new ArrayList<>();
        // List<List<String>> result = new ArrayList<>();

        // for(int i=0; i<strs.length; i++){
        //     if(strs[i] == ""){
        //         data.add(strs[i]);
        //         flag = 0;
        //     }
        //     else{
        //         flag = 1;
        //         String s = sortString(strs[i]);
        //         if(!index.contains(s)){
        //             index.add(s);
        //         }
        //         anagram.put(strs[i], index.indexOf(s));
        //     }
        // }

        // return new ArrayList<>(anagramMap.values());

        // if(flag == 0){
        //     result.add(data);
        //     return result;
        // }

        // int i = 0;
        // while(i != index.size()){
        //     data = new ArrayList<>();

        //     for(Entry<String, Integer> entry : anagram.entrySet()){
        //         if(entry.getValue() == i){
        //             data.add(entry.getKey());
        //         }
        //     }

        //     result.add(data);
        //     i++;
        // }

        // return result;

        Map<String, List<String>> anagramMap = new HashMap<>();

        for (String str : strs) {
            String sortedStr = sortString(str);
            if (!anagramMap.containsKey(sortedStr)) {
                anagramMap.put(sortedStr, new ArrayList<>());
            }
            anagramMap.get(sortedStr).add(str);
        }

        return new ArrayList<>(anagramMap.values());
    }
}