class Solution {
    public int longestConsecutive(int[] nums) {
        if(nums.length == 0 || nums == null){
            return 0;
        }

        Set<Integer> numset = new HashSet<>();
        for(int num : nums){
            numset.add(num);
        }

        int longest = 0;

        for(int num : numset){
            if(!numset.contains(num - 1)){
                int curr = num;
                int streak = 1;

                while(numset.contains(curr + 1)){
                    curr++;
                    streak++;
                }

                longest = Math.max(streak, longest);
            }
        }

        return longest;
    }


}