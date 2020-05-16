参考代码 2：对于是否接在原有序数组后面单独判断，不满足的时候，
再在候选区间的索引范围 [0, size - 1] 内使用二分查找法进行搜索。
class Solution:

    def searchInsert(self, nums: List[int], target: int) -> int:
        # 返回大于等于 target 的索引，有可能是最后一个
        size = len(nums)
        # 特判 1
        if size == 0:
            return 0
        # 特判 2：如果比最后一个数字还要大，直接接在它后面就可以了
        if target > nums[-1]:
            return size

        left = 0
        right = size - 1
        # 二分的逻辑一定要写对，否则会出现死循环或者数组下标越界
        while left < right:
            mid = (left + right) >> 1
            if nums[mid] < target:
                left = mid + 1
            else:
                assert nums[mid] >= target
                right = mid
        return left




参考代码 1：重点理解为什么候选区间的索引范围是 [0, size]。

class Solution:

    def searchInsert(self, nums: List[int], target: int) -> int:
        # 返回大于等于 target 的索引，有可能是最后一个
        size = len(nums)
        # 特判
        if size == 0:
            return 0

        left = 0
        # 如果 target 比 nums里所有的数都大，则最后一个数的索引 + 1 就是候选值，因此，右边界应该是数组的长度
        right = size
        # 二分的逻辑一定要写对，否则会出现死循环或者数组下标越界
        while left < right:
            mid = (left + right) >> 1
            if nums[mid] < target:
                left = mid + 1
            else:
                assert nums[mid] >= target
                # [1,5,7] 2
                right = mid
        # 调试语句
        # print('left = {}, right = {}, mid = {}'.format(left, right, mid))
        return left

给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。

你可以假设数组中无重复元素。

示例 1:

输入: [1,3,5,6], 5
输出: 2
示例 2:

输入: [1,3,5,6], 2
输出: 1
示例 3:

输入: [1,3,5,6], 7
输出: 4
示例 4:

输入: [1,3,5,6], 0
输出: 0

