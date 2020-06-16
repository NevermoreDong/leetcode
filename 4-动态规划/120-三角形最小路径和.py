class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # 自顶向下 O(n**2)空间
        # size = len(triangle)
        # dp = [[0 for _ in range(size)] for _ in range(size)]
        # dp[0][0] = triangle[0][0]
        # for i in range(1, size):
        #     for j in range(i + 1):
        #         if j == 0:
        #             dp[i][j] = dp[i-1][j] + triangle[i][j]
        #         elif j == i:
        #             dp[i][j] = dp[i-1][j-1] + triangle[i][j]
        #         else:
        #             dp[i][j] = min(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j]
        # return min(dp[-1])

        # 自底向上 O(n)空间
        # 如果dp[n]只与dp[n-1]有关，那就可以建O(n)空间，但得自底向上
        size = len(triangle[-1])
        dp = [0 for _ in range(size)]
        for i in range(size):
            dp[i] = triangle[-1][i]
        for i in range(size-2, -1, -1):
            for j in range(i+1):
                dp[j] = min(dp[j], dp[j+1]) + triangle[i][j]
        return dp[0]