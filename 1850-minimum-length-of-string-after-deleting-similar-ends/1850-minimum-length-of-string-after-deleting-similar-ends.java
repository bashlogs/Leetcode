class Solution {
    public int minimumLength(String s) {
        int left = 0;
        int right = s.length()-1;

        while(s.charAt(left) == s.charAt(right) && left < right )
        {
            char target = s.charAt(left);

            while(s.charAt(left) == target && left < right) {
                left++;
            }

            while(s.charAt(right) == target && left <= right) {
                right--;
            }

        }
        return right - left + 1;
    }
}