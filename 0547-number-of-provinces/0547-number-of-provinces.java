class Solution {
    public int findCircleNum(int[][] isConnected) {
        // DFS
        // Stack<Integer> s1 = new Stack<>();
        // int count = 0;
        // boolean[] visited = new boolean[isConnected.length];
        // for(int i=0; i<isConnected.length; i++){
        //     if(!visited[i]){
        //         count++;
        //         s1.push(i);
        //         visited[i] = true;
        //         while(!s1.isEmpty()){
        //             int a = s1.pop();
        //             for(int j=0; j<isConnected[i].length; j++){
        //                 if(isConnected[a][j] == 1 && !visited[j]){
        //                     s1.push(j);
        //                     visited[j] = true;
        //                 }
        //             }
        //         }
        //     }
        // }
        // BFS
        Queue<Integer> s1 = new LinkedList<>();
        int count = 0;
        boolean[] visited = new boolean[isConnected.length];
        for(int i=0; i<isConnected.length; i++){
            if(!visited[i]){
                count++;
                s1.offer(i);
                visited[i] = true;
                while(!s1.isEmpty()){
                    int a = s1.poll();
                    for(int j=0; j<isConnected[i].length; j++){
                        if(isConnected[a][j] == 1 && !visited[j]){
                            s1.offer(j);
                            visited[j] = true;
                        }
                    }
                }
            }
        }
        return count;
    }
}