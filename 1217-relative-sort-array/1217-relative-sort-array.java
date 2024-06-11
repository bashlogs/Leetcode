class Solution {
    public int[] relativeSortArray(int[] arr1, int[] arr2) {
        List<Integer> arr = new ArrayList<>();
        int[] ans = new int[arr1.length];

        for(int i=0; i<arr1.length; i++){
            arr.add(arr1[i]);
        }
        int c = 0;
        for(int i=0; i<arr2.length; i++){
            while(arr.contains(arr2[i])){
                ans[c] = arr2[i];
                arr.remove(arr.indexOf(arr2[i]));
                c++;
            }
        }
        Collections.sort(arr);
        while(arr.size() > 0){
            ans[c] = arr.remove(0);
            c++;
        }
        return ans;
    }
}