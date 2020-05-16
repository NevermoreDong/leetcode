class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # max_cnt = float('-inf')
        # size = len(nums)
        # for left in range(size):
        #     for right in range(left, size):
        #         max_cnt = max(max_cnt, sum(nums[left:right+1]))
        # return max_cnt
        length = len(nums)
        if length == 0: return -2147483648
        dp = [0 for _ in range(length)] # 初始化数组，dp[n]代表前n个数字中的最大子序和
        dp[0] = nums[0]                 # 辅助计算的
        for index in range(1,length):
            if dp[index-1] > 0:         # 如果前面index-1个最大子序和为正，对index数累加有增益
                dp[index] = dp[index-1] + nums[index] # 累加上
            else:
                dp[index] = nums[index] # 为负，无增益，重新起一个开始数字
        return max(dp)