void main(List<String> args) {
  var grid = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "1"],
    ["0", "0", "1", "1", "0"]
  ];

  int numIslands(List<List<String>> grid) {
    int count = 0;
    if (grid.isEmpty) return 0;
    int r = grid.length;
    int c = grid[0].length;
    void dfs(x, y, r, c) {
      grid[x][y] = '0';
      if (x != 0 && grid[x - 1][y] == '1') dfs(x - 1, y, r, c);
      if (x != r - 1 && grid[x + 1][y] == '1') dfs(x + 1, y, r, c);
      if (y != 0 && grid[x][y - 1] == '1') dfs(x, y - 1, r, c);
      if (y != c - 1 && grid[x][y + 1] == '1') dfs(x, y + 1, r, c);
    }

    for (int i = 0; i < r; i++) {
      for (int j = 0; j < c; j++) {
        if (grid[i][j] == '1') {
          count++;
          dfs(i, j, r, c);
        }
      }
    }
    return count;
  }

  var numIslands2 = numIslands(grid);
    print(numIslands2);
}
