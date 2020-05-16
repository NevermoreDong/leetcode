class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # # m为列，n为行
        # # 递归写法，此方法超时，用动态规划
        # def dfs(row, col, path):
        #     if row == n-1 and col == m-1:
        #         res.append(path)

        #     d_row, d_col = row + 1, col  # 向下走
        #     if d_row < n and d_col < m:
        #         path.append([d_row, d_col])
        #         dfs(d_row, d_col, path)

        #     r_row, r_col = row, col + 1  # 向右走
        #     if r_row < n and r_col < m:
        #         path.append([r_row, r_col])
        #         dfs(r_row, r_col, path)
        # if n == 0: return 1
        # path, res = [[0,0]], []
        # dfs(0, 0, path)
        # return len(res)

        # m为列，n为行
        # 我们令dp[i][j]是到达i, j最多路径
        # 动态方程：dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        # 注意，对于第一行dp[0][j]，或者第一列dp[i][0]，由于都是在边界，所以只能为1
        # 时间复杂度：O(m * n)
        # 空间复杂度：O(m * n)
        dp = [[0 for _ in range(m)]  for _ in range(n)]
        for col in range(m):
            dp[0][col] = 1
        for raw in range(n):
            dp[raw][0] = 1
        for col in range(1, m):
            for raw in range(1, n):
                dp[raw][col] = dp[raw-1][col] + dp[raw][col-1]
        return dp[-1][-1]

# 优化1：空间复杂度 O(2n)O(2n)
# class Solution:
#     def uniquePaths(self, m: int, n: int) -> int:
#         pre = [1] * n
#         cur = [1] * n
#         for i in range(1, m):
#             for j in range(1, n):
#                 cur[j] = pre[j] + cur[j-1]
#             pre = cur[:]
#         return pre[-1]

# 优化2：空间复杂度 O(n)
# class Solution:
#     def uniquePaths(self, m: int, n: int) -> int:
#         cur = [1] * n
#         for i in range(1, m):
#             for j in range(1, n):
#                 cur[j] += cur[j-1]
#         return cur[-1]




