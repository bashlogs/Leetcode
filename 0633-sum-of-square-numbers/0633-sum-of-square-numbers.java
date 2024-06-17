class Solution {
    public boolean judgeSquareSum(int c) {
        if(c <= 2){
            return true;
        }

        int times = (int) Math.ceil(Math.sqrt(c));
        Set<Integer> check = new HashSet<>();
        check.add(0);

        for(int i=times; i>0; i--){
            int a = i * i;
            check.add(a);
            if(check.contains(c-a)){
                System.out.println(check);
                return true;
            }
        }

        return false;
    }
}