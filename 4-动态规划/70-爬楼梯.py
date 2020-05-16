class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1: return 1
        dp = [0 for i in range(n+1)]
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n+1):
        	dp[i] = dp[i-1] + dp[i-2]
        return dp[i]

    # def climbStairs(self, n: int) -> int:
    # 	dp = [0 for i in range(n)]
    # 	dp[0], dp[1] = 1, 2
    # 	for i in range(2, n):
    # 		dp[i] = dp[i-1] + dp[i-2]
    # 	return dp[n-1]




# class Solution {
# public:
#     int climbStairs(int n) {
#         if(n==1) return 1;
#         vector<int> s(n+1,-1);
#         s[1]=1;
#         s[2]=2;
#         for(int i=3;i<=n;i++)
#         {
#             s[i]=s[i-1]+s[i-2];
#         }
#         return s[n];
#     }
# };

