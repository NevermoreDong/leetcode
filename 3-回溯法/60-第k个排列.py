'''
回溯，得到所有的结果，返回第K个
'''
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        def dfs(path, depth):
            if depth == n:
                res.append(''.join(path))
                return 
            for i in range(n):
                str_num = str(i+1)
                if str_num in path:
                    continue
                path.append(str_num)
                dfs(path, depth+1)
                path.pop()
        path, res = [], []
        dfs(path, 0)
        return res[k-1]

'''
回溯到第K个，就跳出递归,重点学习下跳出递归的写法
'''
class Solution:
    def getPermutation(n, k):
        self.cnt = 0
        def dfs(path, depth):
            if depth == n:
                res.append(''.join(path))
                self.cnt += 1

                if self.cnt == k: # 后剪枝
                    return True   ###
            for i in range(n):

                str_num = str(i + 1)
                if str_num in path:
                    continue
                path.append(str_num)
                if dfs(path, depth + 1):
                    return True   ###
                path.pop()
            return False   ###
        path, res = [], []
        tmp = dfs(path, 0)
        return res[-1]



'''
解题思路：

明显该题目是只求第K个排列，不需要枚举所有排列。那么如何提前返回（减枝）呢。

每个分支的排列数量count是可以求出来的，(n-1)!
如果k大于count，说明第K个不在此分支，k减去该分支的数量，进行同层下一个分支的判断
如果小于count，说明在此分支，则进入下一层，继续按照上面的规则递归

这种回溯法，写法上有小技巧：比如每次都有path（已经遍历的路径）和remain（剩余需要遍历的节点）
复杂度分析：
Space：O(N)
Time: O(N^2) 最坏需要1+2+...+n次比较
'''
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        def factorial(n):
            res = 1
            while n:
                res *= n
                n -= 1
            return res
        def dfs(path, remain, k):
            if not remain: 
                return path         # 找到一个结果就跳出递归，返回答案 
            length = len(remain)
            lower_possible_cnt = factorial(length-1) # # 对于每一层，该层每个分支的数量相当于剩余数量-1的阶乘
            for i in range(length):
                if k > lower_possible_cnt: # 此处如果k大于该分支排列数量，那么减去该分支
                    k -= lower_possible_cnt
                else:
                    path.append(remain[i])
                    remain = remain[:i]+remain[i+1:]
                    return dfs(path, remain, k)

        result = dfs([], [str(i+1) for i in range(n)] ,k)
        return ''.join(result)



