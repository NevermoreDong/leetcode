class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        if not s: return []
        def dfs(path, residue):

            if len(residue) == 0:
                res.append(path[:])
                return
            for cut_length in range(1, len(residue)+1):
                cut = residue[:cut_length]
                if cut == cut[::-1]:
                    path.append(cut)
                    dfs(path, residue[cut_length:])
                    path.pop()

        res = []
        dfs([], s)
        return res
            