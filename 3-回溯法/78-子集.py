class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def dfs(path, start):
            res.append(path[:])
            if len(path) == len(nums):
                return
            for index in range(start, len(nums)):
                path.append(nums[index])
                dfs(path, index+1)
                path.pop()
        
        res = []
        dfs([], 0)
        return res