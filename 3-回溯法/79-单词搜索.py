class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # 标准的回溯剪枝，找到一个答案就中途退出
        rows = len(board)
        cols = len(board[0])

        def dfs(row, col, deep, path):
            if deep == len(word):
                return True
            for dr, dc in [(0,1), (0,-1), (1,0), (-1,0)]:
                row_tmp = row + dr
                col_tmp = col + dc
                if 0 <= row_tmp < rows and 0 <= col_tmp < cols \
                        and (row_tmp, col_tmp) not in path \
                        and word[deep] == board[row_tmp][col_tmp]:
                    path.append((row_tmp, col_tmp))
                    if dfs(row_tmp, col_tmp, deep+1, path):
                        return True
                    path.pop()

            return False

        for r in range(rows):
            for c in range(cols):
                # 控制起点
                if word[0] == board[r][c] and dfs(r, c, 1, [(r, c)]):
                    return True
        return False 