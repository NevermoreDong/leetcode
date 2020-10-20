def solution(candidates, target):

    def dfs(path, path_cnt, begin):
        if path_cnt == target:
            res.append(path[:])
        for i in candidates[begin:]:
            if path_cnt + i <= target:
                path.append(i)
                dfs(path, path_cnt + i, candidates.index(i))
                path.pop()
    res = []
    dfs([], 0, 0)
    return res






if __name__ == "__main__":
    candidates = [2,3,5]
    target = 8
    res = solution(candidates, target)
    print(res)

test from cp
