class Solution {
    public int bestClosingTime(String customers) {
        int cur_penalty = 0;
        for(int i=0; i<customers.length(); i++){
            if(customers.charAt(i) == 'Y'){
                cur_penalty++;
            }
        }
        int min_penalty = cur_penalty;
        int early = 0;
        for(int i=0; i<customers.length(); i++){
            char ch = customers.charAt(i);
            if(ch == 'Y'){
                cur_penalty--;
            }
            else{
                cur_penalty++;
            }

            if(cur_penalty < min_penalty){
                early = i+1;
                min_penalty = cur_penalty;
            }
        }
        return early;
    }
}