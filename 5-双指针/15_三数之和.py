'''
给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。

注意：答案中不可以包含重复的三元组。

例如, 给定数组 nums = [-1, 0, 1, 2, -1, -4]，

满足要求的三元组集合为：
[
  [-1, 0, 1],
  [-1, -1, 2]
]
'''
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        size = len(nums)
        res = []
        nums.sort()
        for i in range(size-2):
            if i>0 and nums[i] == nums[i-1]:
                continue
            l = i+1
            r = size-1
            target = -nums[i]
            while l<r:
                if nums[l]+nums[r] == target:
                    res.append([nums[i],nums[l],nums[r]])
                    l += 1
                    r -= 1
                    while l<r and nums[l] == nums[l-1]:
                        l += 1
                    while l<r and nums[r] == nums[r+1]:
                        r -= 1
                elif nums[l]+nums[r] < target:
                    l += 1
                else:
                    r -= 1
        return res

