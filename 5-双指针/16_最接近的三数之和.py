'''
给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。返回这三个数的和。假定每组输入只存在唯一答案。

例如，给定数组 nums = [-1，2，1，-4], 和 target = 1.

与 target 最接近的三个数的和为 2. (-1 + 2 + 1 = 2).
'''
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        res = 0
        diff = float('inf')
        size = len(nums)
        nums.sort()
        for i in range(size-2):
            l = i+1
            r = size-1
            while l<r:
                sum_ = nums[i]+nums[l]+nums[r]
                if sum_ < target:
                    if abs(sum_ - target) < diff:
                        diff = abs(sum_ - target)
                        res = sum_
                    l += 1
                else:
                    if abs(sum_ - target) < diff :
                        diff = abs(sum_ - target )
                        res = sum_
                    r -= 1
        return res