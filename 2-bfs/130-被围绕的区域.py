class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        ## bfs
        # if not board or not board[0]:
        #     return
        # rows, cols = len(board), len(board[0])
        # def bfs(row, col):
        #     queue = [(row, col)]
        #     while queue:
        #         node_r, node_c = queue.pop(0)
        #         if 0 <= node_r < rows and 0 <= node_c < cols and board[node_r][node_c] == 'O':
        #             board[node_r][node_c] = 'B'
        #             for dr, dc in [(0,1), (1,0), (0,-1), (-1,0)]:
        #                 queue.append((node_r+dr, node_c+dc))

        # for row in range(rows): #判断左右两边是否有0
        #     if board[row][0] == 'O':
        #         bfs(row, 0)
        #     if board[row][cols-1] == 'O':
        #         bfs(row, cols-1)

        # for col in range(cols): # 判断上下两边是否有0
        #     if board[0][col] == 'O':
        #         bfs(0, col)
        #     if board[rows-1][col] == 'O':
        #         bfs(rows-1, col)

        # for r in range(rows):
        #     for c in range(cols):
        #         if board[r][c] == 'O':
        #             board[r][c] = 'X'
        #         if board[r][c] == 'B':
        #             board[r][c] = 'O'

        ## dfs 
        if not board or not board[0]:
            return
        rows, cols = len(board), len(board[0])

        def dfs(row, col):
            board[row][col] = 'B'
            for dr, dc in [(0,1), (1,0), (0,-1), (-1,0)]:
                cur_row = row + dr
                cur_col = col + dc
                if 0 <= cur_row < rows and 0 <= cur_col < cols and board[cur_row][cur_col] == 'O':
                    dfs(cur_row, cur_col)

        for row in range(rows): #判断左右两边是否有0
            if board[row][0] == 'O':
                dfs(row, 0)
            if board[row][cols-1] == 'O':
                dfs(row, cols-1)

        for col in range(cols): # 判断上下两边是否有0
            if board[0][col] == 'O':
                dfs(0, col)
            if board[rows-1][col] == 'O':
                dfs(rows-1, col)

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                if board[r][c] == 'B':
                    board[r][c] = 'O'