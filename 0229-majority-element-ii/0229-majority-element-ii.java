class Solution {
    public List<Integer> majorityElement(int[] nums) {
        
        HashMap<Integer, Integer> a1 = new HashMap<>();
        int maxCount = 0;
        for (int num : nums) {
            a1.put(num, a1.getOrDefault(num, 0) + 1);
            maxCount = Math.max(maxCount, a1.get(num));
        }

        ArrayList<Integer> b1 = new ArrayList<>();
        int a = nums.length/3;
        System.out.println(a);
        for(Map.Entry<Integer, Integer> e : a1.entrySet()){
            if(e.getValue() > a){
                b1.add(e.getKey());
            }
        }

        return b1;
    }
}