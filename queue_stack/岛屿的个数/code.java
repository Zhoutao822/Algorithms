import java.util.ArrayList;
import java.util.List;

public class code {
    public static void main(String[] args) {
        char[][] grid = { 
            { '1', '1', '1', '1', '0' }, 
            { '1', '1', '0', '1', '0' }, 
            { '1', '1', '0', '0', '1' },
            { '0', '1', '1', '0', '0' } };
        
        System.out.print(String.valueOf(code.numIslands(grid)));
    }

    public static int numIslands(char[][] grid) {
        int count = 0;
        if (grid == null || grid.length == 0) {
            return 0;
        }
        int r = grid.length;
        int c = grid[0].length;
        for (int i = 0; i < r; i++) {
            for (int j = 0; j < c; j++) {
                if (grid[i][j] == '1') {
                    count++;
                    dfs(i, j, r, c, grid);
                }
            }
        }
        return count;
    }

    private static void dfs(int x, int y, int r, int c, char[][] grid) {
        grid[x][y] = '0';
        if (x != 0 && grid[x - 1][y] == '1') {
            dfs(x - 1, y, r, c, grid);
        }
        if (x != r - 1 && grid[x + 1][y] == '1') {
            dfs(x + 1, y, r, c, grid);
        }
        if (y != 0 && grid[x][y - 1] == '1') {
            dfs(x, y - 1, r, c, grid);
        }
        if (y != c - 1 && grid[x][y + 1] == '1') {
            dfs(x, y + 1, r, c, grid);
        }
    }
}