class Solution:
    def numDecodings(self, s: str) -> int:
    	n = len(s)
        if n==0: return 0
        dp = [0 for i in range(n+1)]	# dp[n]表示第n个数字有多少可能
        dp[0] = 1						# 自定义，辅助后面计算
        dp[1] = 1 if s[0]!='0' else 0 	# s的第一个数字是否为0
        for i in range(2,n+1):
        	if s[i-1] != '0':			# s的第i个数字s[i-1]是否为0
        		dp[i] += dp[i-1]		# 如果不为0，dp[i]等于前面的那一位，
        								# 如果为0，就舍弃解码一个数字的可能
        	if '10' <= s[i-2:i] <= '26':# s的i-1、i个数字s[i-2:i]是不是在10到26之间
        								# 如果在<10或>26其实就是上面的可能
        		dp[i] += dp[i-2]		# 如果在，dp[i]就累加上从dp[i-2]解码两位的可能
        return dp[n]



