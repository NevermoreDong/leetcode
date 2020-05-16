class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def dfs(path, begin, length):
            if length == k:
                res.append(path[:])
                return
            for index in range(begin, n):
                path.append(candidates[index])
                dfs(path, index+1, length+1)
                path.pop()
        candidates = [i for i in range(1, n+1)]
        res = []
        dfs([], 0, 0)
        return res