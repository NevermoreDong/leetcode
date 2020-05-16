class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def dfs(graph, row_cnt):
            if row_cnt == len(graph):
                tmp = []
                for _row in graph:
                    strs = ''.join(_row)
                    tmp.append(strs)
                res.append(tmp)
            for col in range(n):
                if not isvalid(graph, row_cnt, col):
                    continue
                graph[row_cnt][col] = 'Q'
                dfs(graph, row_cnt+1)
                graph[row_cnt][col] = '.'

        def isvalid(graph, row, col):
            for i in range(n):
                if graph[i][col] == 'Q':
                    return False
            r_row, r_col = row, col
            while r_row >=0 and r_col <= n-1:
                if graph[r_row][r_col] == 'Q':
                    return False
                r_row -= 1
                r_col += 1
            l_row, l_col = row, col
            while l_row >= 0 and l_col >= 0:
                if graph[l_row][l_col] == 'Q':
                    return False
                l_row -= 1
                l_col -= 1
            return True
        
        graph = [['.' for _ in range(n)] for _ in range(n)]
        res = []
        dfs(graph, 0)
        return res