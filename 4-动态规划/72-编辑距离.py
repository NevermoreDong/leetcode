class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # dp[i][j] 为word1前i个字符转化为word2前j个字符
        size1 = len(word1) + 1 # 有个空的字符串""
        size2 = len(word2) + 1
        dp = [[0 for _ in range(size2)] for _ in range(size1)]
        for r in range(1, size2):
            dp[0][r] = dp[0][r-1] + 1
        for c in range(1, size1):
            dp[c][0] = dp[c-1][0] + 1
        for i in range(1, size1):
            for j in range(1, size2):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
        return dp[-1][-1]