class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        size = len(candidates)
        if size == 0: return []
        
        def dfs(candidates, begin, target):
            if target == 0 and path[:] not in res:
                res.append(path[:])
            for index in range(begin, size):
                residue = target - candidates[index]
                if residue < 0:
                    break
                if index > begin and candidates[index] == candidates[index-1]:
                    continue #跳到下个不同的数
                path.append(candidates[index])
                dfs(candidates, index+1, residue)
                path.pop()     
        path, res = [], []
        dfs(candidates, 0, target)
        return res

#利用 not in 去重
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        size = len(candidates)
        if size == 0: return []
        
        def dfs(candidates, begin, size, path, res, target):
            if target == 0 and path[:] not in res:
                res.append(path[:])
            for index in range(begin, size):
                residue = target - candidates[index]
                if residue < 0:
                    break
                path.append(candidates[index])
                dfs(candidates, index+1, size, path, res, residue)
                path.pop()
        
        path, res = [], []
        dfs(candidates, 0, size, path, res, target)
        return res