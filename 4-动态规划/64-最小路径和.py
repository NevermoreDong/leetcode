class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # dp[col][row]为到达(col, row)的路径最小数字和
        cols, rows = len(grid), len(grid[0])
        # 初始化
        dp = [[0 for _ in range(rows)] for _ in range(cols)]
        dp[0][0] = grid[0][0]
        for r in range(1, rows):   # 初始化第一行
            dp[0][r] = dp[0][r-1] + grid[0][r]
        for c in range(1, cols):   # 初始化第一列
            dp[c][0] = dp[c-1][0] + grid[c][0]

        for row in range(1, rows):
            for col in range(1, cols):
                dp[col][row] = min(dp[col-1][row], dp[col][row-1]) + grid[col][row]

        return dp[-1][-1]