package leet_code_java;

public class Array_2d_problem {
    // 200. Number of Islands
    private int m;
    private int n;

    public int numIslands(char[][] grid){
        int count=0;
        n = grid.length;    // n 行
        if (n==0) return 0;
        m = grid[0].length;     // m列
        for (int i=0; i<n; i++){
            for (int j=0; j<m; j++){
                if (grid[i][j] == '1'){
                    DFSMarking(grid, i, j);
                    ++count;
                }
            }
        }
        return count;
    }
    private void DFSMarking(char[][] grid, int i, int j){
        if(i<0||j<0 || i>=n || j>= m || grid[i][j] != '1') return;
        grid[i][j] = '0';
        DFSMarking(grid, i+1, j);
        DFSMarking(grid, i-1, j);
        DFSMarking(grid, i, j+1);
        DFSMarking(grid, i, j-1);
    }

    public static void main(String[] args){

    }
}
