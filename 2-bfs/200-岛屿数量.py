def sol(grid):
    cnt = 0
    row = len(grid)
    col = len(grid[0])
    def bfs(site):
        queue = [(site[0], site[1])]
        while queue:
            node = queue.pop(0)
            r, c = node[0], node[1]
            for dr, dc in [(1,0), (0,1), (-1,0), (0,-1)]:
                cur_r = r + dr
                cur_c = c + dc
                if 0<=cur_r<row and 0<=cur_c<col and grid[cur_r][cur_c]=='1':
                    grid[cur_r][cur_c] = '0'
                    queue.append((cur_r, cur_c))
    def dfs(r, c):
        grid[r][c] = "0"
        for dr, dc in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            cur_r = r + dr
            cur_c = c + dc
            if 0 <= cur_r < row and 0 <= cur_c < col and grid[cur_r][cur_c] == '1':
                dfs(cur_r, cur_c)

    for i in range(row):
        for j in range(col):
            if grid[i][j] == '1':
                dfs(i, j)
                cnt += 1
    return cnt

if __name__ == '__main__':
    gird = [["1","1","0","1","0"],
            ["1","1","0","1","0"],
            ["1","1","0","0","0"],
            ["0","0","0","1","0"]]
    result = sol(gird)
    print(result)

