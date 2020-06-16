题目要求O（logN）的时间复杂度，基本可以断定本题是需要使用二分查找，怎么分是关键
由于题目说数字了无重复，举个例子
1 2 3 4 5 6 7 可以大致分为两类,
第一类 2 3 4 5 6 7 1 这种，也就是nums[start] <= nums[mid]。此例子中就是2 <= 5
这种情况下，前半部分有序。因此如果 nums[start] <=target<nums[mid]。则在前半部分找，
否则去后半部分找。
第二类 6 7 1 2 3 4 5 这种，也就是nums[start] > nums[mid]。此例子中就是6 > 2
这种情况下，后半部分有序。因此如果 nums[mid] <target<=nums[end]。则在后半部分找，
否则去前半部分找。

参考这里，算法基于一个事实，数组从任意位置劈开后，至少有一半是有序的，什么意思呢？
比如 [ 4 5 6 7 1 2 3] ，从 7 劈开，左边是 [ 4 5 6 7] 右边是 [ 7 1 2 3]，左边是有序的。
基于这个事实。
我们可以先找到哪一段是有序的 (只要判断端点即可)，然后看 target 在不在这一段里，
如果在，那么就把另一半丢弃。如果不在，那么就把这一段丢弃。

# 中间元素和右边界比较，使用左中位数
class Solution:
    def search(self, nums, target):
        size = len(nums)
        if size == 0:
            return -1
        left = 0
        right = size - 1
        while left < right:
            # mid = left + (right - left) // 2
            mid = (left + right) >> 1
            if nums[mid] < nums[right]:
                # 右半部分有序
                if nums[mid + 1] <= target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid
            else:
            	# 左半边有序 使用二分法，一定要在有序的一侧进行
                if nums[left] <= target <= nums[mid]:
                    right = mid
                else:
                    left = mid + 1
        # 后处理
        return left if nums[left] == target else -1

# 不是模板解法，自己天然想法

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        size = len(nums)
        if size == 0: return -1
        left = 0
        right = size - 1
        while left < right :
            mid = (left + right) >> 1
            if target == nums[mid]:
                return mid
            if nums[mid] < nums[right]:
                if nums[mid+1] <= target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                if nums[left] <= target <= nums[mid-1]:
                    right = mid - 1
                else:
                    left = mid + 1
        return left if nums[left] == target else -1

