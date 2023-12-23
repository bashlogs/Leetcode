class Solution {
    public boolean isPathCrossing(String path) {
        Set<String> visited = new HashSet<>();
        int currX = 0, currY = 0;
        visited.add(currX + "," + currY);
        for(char dir : path.toCharArray()){
            if(dir == 'N') currY++;
            else if(dir == 'S') currY--;
            else if(dir == 'E') currX++;
            else currX--;

            String add = currX + "," + currY;
            if(visited.contains(add)){
                return true;
            }
            visited.add(add);
        }
        return false;
    }
}