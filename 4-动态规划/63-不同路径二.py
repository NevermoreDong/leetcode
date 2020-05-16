class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        all_raws, all_col = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0 for _ in range(all_col)] for _ in range(all_raws)]
        dp[0][0] = 1 if obstacleGrid[0][0] != 1 else 0  # 起点就阻塞
        if dp[0][0] == 0: return 0
        for i in range(1, all_col):     # 初始化第一行，初始化很重要
            if obstacleGrid[0][i] != 1: # 根据移动性质，如果遇到一个阻塞点，后面的都会被阻塞
                dp[0][i] = 1
            else:
                break
        for i in range(1, all_raws):    # 初始化第一列
            if obstacleGrid[i][0] != 1: # # 如果遇到一个阻塞点，后面的都会被阻塞
                dp[i][0] = 1
            else:
                break
        for raw in range(1, all_raws):
            for col in range(1, all_col):
                if obstacleGrid[raw][col] != 1: # 遇到阻塞就跳过
                    dp[raw][col] = dp[raw - 1][col] + dp[raw][col - 1]
        return dp[-1][-1]