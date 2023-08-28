class MyStack {

    int top;
    int last;
    int[] stack = new int[100];
    
    public MyStack() {
        top = -1;
        last = -1;
    }
    
    public void push(int x) {
        if(last == -1 && top == -1){
            last = top = 0;
        }
        stack[++top] = x;

    }
    
    public int pop() {
        return stack[top--];
    }
    
    public int top() {
        return stack[top];
    }
    
    public boolean empty() {
        if(top == -1 || last == top){
            return true;
        }
        else{
            return false;
        }
    }
}

/**
 * Your MyStack object will be instantiated and called as such:
 * MyStack obj = new MyStack();
 * obj.push(x);
 * int param_2 = obj.pop();
 * int param_3 = obj.top();
 * boolean param_4 = obj.empty();
 */