class Solution {
    public int[] searchRange(int[] nums, int target) {
        int[] arr = {-1,-1};
        int left=0;
        int right=nums.length-1;
        while(left<=right){
            int mid = left+(right-left)/2;
            if(nums[mid] == target){
                int start = mid;
                while(start > 0 && nums[start-1] == target){
                    start--;
                }
                int end = mid;
                while(end < nums.length-1 && nums[end+1] == target){
                    end++;
                }
                arr[0] = start;
                arr[1] = end;
                return arr;
            }
            else if(nums[mid] < target){
                left = mid+1;
            }
            else{
                right = mid-1;
            }
        }
        return arr;
    }
}