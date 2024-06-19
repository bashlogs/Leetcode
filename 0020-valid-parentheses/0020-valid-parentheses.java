class Solution {
    public boolean isValid(String s) {
        Stack<Character> para = new Stack<>();

        for(int i=0; i<s.length(); i++){
            char current = s.charAt(i);

            if(current == '(' || current == '{' || current == '['){
                para.push(current);
            }
            else if(!para.isEmpty() && current == ')' && para.peek() == '('){
                para.pop();
                continue;
            }
            else if(!para.isEmpty() && current == '}' && para.peek() == '{'){
                para.pop();
                continue;
            }
            else if(!para.isEmpty() && current == ']' && para.peek() == '['){
                para.pop();
                continue;
            }
            else{
                return false;
            }
        }

        return (para.isEmpty()) ? true : false;
    }
}