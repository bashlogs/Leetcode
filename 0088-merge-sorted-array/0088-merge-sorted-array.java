class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        int i = 0;
        int j = 0;
        int c = -1;
        int[] _array = new int[m+n];

        while(i != m || j != n){
            if(i == m){
                System.out.println("Hello");
                _array[++c] = nums2[j];
                j++;
            }
            else if(j == n){
                _array[++c] = nums1[i];
                i++;
            }
            else{
                if(nums1[i] <= nums2[j]){
                    _array[++c] = nums1[i];
                    i++;
                }
                else{
                    _array[++c] = nums2[j];
                    j++;
                }
            }
        }

        for(i=0; i<_array.length; i++){
            nums1[i] = _array[i];
        }
    }
}