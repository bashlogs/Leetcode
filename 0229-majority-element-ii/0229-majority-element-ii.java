class Solution {
    public List<Integer> majorityElement(int[] nums) {
        // HashMap<Integer, Float> a1 = new HashMap<>();
        // ArrayList<Integer> b1 = new ArrayList<>();
        // float count = 0;
        // float mid = nums.length/3;
        // System.out.println(mid);
        // a1.put(nums[0], mid);

        // for(int i=1; i<nums.length; i++){
        //     if(a1.containsKey(nums[i])){
        //         count = a1.get(nums[i]);
        //         a1.put(nums[i], count + mid);
        //     }
        //     else{
        //         a1.put(nums[i],mid);
        //     }
        //     System.out.println("Updated Map " + a1);
        // }

        // for(int i=0; i<nums.length; i++){
        //     if(a1.getValue(i) >= mid){
        //         b1.add(a1.getKey(i));
        //     }
        // }

        // for(Map.Entry<Integer, Float> e : a1.entrySet()){
        //     if(e.getValue() > mid){
        //         b1.add(e.getKey());
        //     }
        //     else if(nums.length < 3){
        //         b1.add(e.getKey());
        //     }
        // }

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