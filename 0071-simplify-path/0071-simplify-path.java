class Solution {
    public String simplifyPath(String path) {
        String[] paths = path.split("/");
        Stack<String> data = new Stack<>();

        for(int i=0; i<paths.length; i++){
            if(paths[i] == "" || paths[i].equals(".")){
                continue;
            }
            else if(paths[i].equals("..")){
                if(!data.isEmpty()){
                    data.pop();
                }
            }
            else{
                data.push(paths[i]);
            }
        }

        String ans = "";
        while(!data.isEmpty()){
            if(data.peek() != "."){
                ans = "/" + data.pop() + ans;
            }
        }
        
        return (ans.length() == 0) ? "/" : ans;
    }
}