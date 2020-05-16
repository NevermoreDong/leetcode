class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        size = len(candidates)
        if size == 0:
            return []

        # 剪枝的前提是数组元素排序
        # 深度深的边不能比深度浅的边还小
        # 要排序的理由：1、前面用过的数后面不能再用；2、下一层边上的数不能小于上一层边上的数。
        candidates.sort()
        # 在遍历的过程中记录路径，一般而言它是一个栈
        path = []
        res = []
        # 注意要传入 size ，在 range 中， size 取不到
        self.__dfs(candidates, 0, size, path, res, target)
        return res

    def __dfs(self, candidates, begin, size, path, res, target):
        # 先写递归终止的情况
        if target == 0:
            # Python 中可变对象是引用传递，因此需要将当前 path 里的值拷贝出来
            # 或者使用 path.copy()
            res.append(path[:])

        for index in range(begin, size):
            residue = target - candidates[index]
            # “剪枝”操作，不必递归到下一层，并且后面的分支也不必执行
            if residue < 0:
                break
            path.append(candidates[index])
            # 因为下一层不能比上一层还小，起始索引还从 index 开始
            self.__dfs(candidates, index, size, path, res, residue)
            path.pop()

#把dfs的函数定义放在combinationSum函数中，可以不用传重复的参数
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        size = len(candidates)
        if size == 0:
            return []
        candidates.sort()
        path = []
        res = []

        def dfs(candidates, begin, target):
            if target == 0:
                res.append(path[:])

            for index in range(begin, size):
                residue = target - candidates[index]
                if residue < 0:
                    break
                path.append(candidates[index])
                dfs(candidates, index, residue)
                path.pop()
                
        dfs(candidates, 0, target)
        return res
# 改写成加法
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        size = len(candidates)
        if size == 0 : return []
        
        def dfs(candidates, begin, count):
            if count == target:
                res.append(path[:])
            for index in range(begin, size):
                _sum = count + candidates[index]
                if _sum > target:
                    break
                path.append(candidates[index])
                dfs(candidates, index, _sum)
                path.pop()
        
        path = []
        res = []
        count = 0
        dfs(candidates, 0, count)
        return res