class MinStack {
    Stack<Integer> s1;
    Stack<Integer> min;
    public MinStack() {
        s1 = new Stack<>();
        min = new Stack<>();
    }
    
    public void push(int val) {
        s1.push(val);
        if(min.isEmpty() || min.peek() >= val){
            min.push(val);
        }
    }
    
    public void pop() {
        if(s1.isEmpty()){
            return;
        }
        int m = s1.pop();
        if(m == min.peek()){
            min.pop();
        }
    }
    
    public int top() {
        return s1.peek();
    }
    
    public int getMin() {
        if(!min.isEmpty()){
            return min.peek();
        }
        return 0;
    }
    
}

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack obj = new MinStack();
 * obj.push(val);
 * obj.pop();
 * int param_3 = obj.top();
 * int param_4 = obj.getMin();
 */