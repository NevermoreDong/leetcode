class Solution:
    def totalNQueens(self, n: int) -> int:
        graph = [['.' for _ in range(n)] for _ in range(n)]
        res = []

        def dfs(graph, row_cnt):
            if row_cnt == n:
                reset_graph = []
                for every_row in graph:
                    reset_graph.append(''.join(every_row))
                res.append(reset_graph)
                return
            for col_cnt in range(n):
                if not isvaild(graph, row_cnt, col_cnt):
                    continue
                graph[row_cnt][col_cnt] = 'Q'
                dfs(graph, row_cnt+1)
                graph[row_cnt][col_cnt] = '.'

        def isvaild(graph, cur_row, cur_col):
            # 上面有没有
            for i in range(cur_row+1):
                if graph[i][cur_col] == 'Q':
                    return False
            # 右上有没有
            r_row, r_col = cur_row, cur_col
            while r_row >= 0 and r_col <= n-1:
                if graph[r_row][r_col] == 'Q':
                    return False
                r_row -= 1
                r_col += 1
            # 左上有没有
            l_row, l_col = cur_row, cur_col
            while l_row >= 0 and l_col >= 0:
                if graph[l_row][l_col] == 'Q':
                    return False
                l_row -= 1
                l_col -= 1
            return True

        dfs(graph, 0)
        return len(res)