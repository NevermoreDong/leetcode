class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix: return False
        if not matrix[0]: return False
        # 从右上角开始找，从左下角也可以，
        # 但是不能从左上和右下，因为当遍历点大于或小于target时，raw和col不知道改怎么变化
        # raws, cols = len(matrix), len(matrix[0])
        # raw, col = 0, cols-1
        # while raw < raws and col >= 0:
        #     if matrix[raw][col] == target:
        #         return True
        #     elif matrix[raw][col] < target:
        #         raw += 1
        #     elif matrix[raw][col] > target:
        #         col -= 1
        # return False
        # raw, col = raws-1, 0
        # while raw >= 0 and col < cols:
        #     if matrix[raw][col] == target:
        #         return True
        #     elif matrix[raw][col] < target:
        #         col += 1
        #     elif matrix[raw][col] > target :
        #         raw -= 1
        # return False
        # 方法二:二分查找
        raws, cols = len(matrix), len(matrix[0])
        # 进行行二分，定位行
        low, high = 0, raws-1
        while low <= high:
            mid = (low + high) >> 1
            if matrix[mid][0] <= target <= matrix[mid][-1]:
                break
            elif target > matrix[mid][-1]:
                low = mid + 1
            elif target < matrix[mid][0]:
                high = mid -1
        # 在定位的行里，列二分
        real_row = mid
        low, high = 0, cols-1
        while low <= high: # 得有个等于，定位到最后一个得进循环看看是不是等于target
            mid = (low + high) >> 1
            if target == matrix[real_row][mid]:
                return True
            elif target > matrix[real_row][mid]:
                low = mid + 1
            elif target < matrix[real_row][mid]:
                high = mid - 1
        return False