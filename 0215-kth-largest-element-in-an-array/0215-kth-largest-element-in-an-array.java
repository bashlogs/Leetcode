class Solution {

    void minheap(int[] nums, int i, int size){
        int max = i;
        int left = 2*max;
        int right = 2*max+1;
        if(left < size && nums[left] < nums[max]){
            max = left;
        }
        if(right < size && nums[right] < nums[max]){
            max = right;
        }
        if(i != max){
            int t = nums[i];
            nums[i] = nums[max];
            nums[max] = t;
            minheap(nums, max, size);
        }
    }

    void print(int[] nums, int size){
        for(int i=0; i<size; i++){
            System.out.print(nums[i]+"\t");
        }
    }

    void heapsort(int a[], int size){
        int i, t;
        for(i=size-1; i > 0; i--){
            t = a[0];
            a[0] = a[i];
            a[i] = t;
            minheap(a,0,i);
        }
    }


    public int findKthLargest(int[] nums, int k) {
        int size=nums.length;
        int a = 0;
        for(int i=size/2-1; i >= 0; i--){
            minheap(nums, i, size);
            
        }
        heapsort(nums,size);
        print(nums, size);
        return nums[k-1];
    }
}