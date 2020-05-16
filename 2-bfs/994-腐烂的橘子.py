class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        queue = [] #坏橘子位置
        count = 0 # 好橘子数量

        for r in range(row):
            for c in range(col):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    count += 1

        round_count = 0 #腐烂的轮数
        while len(queue) > 0 and count > 0: # 还有好橘子且队列还有坏橘子
            round_count += 1                # 层数+1
            bad_count = len(queue)          # 记录这一层的坏橘子数
            for i in range(bad_count):      # 遍历完这一层的坏橘子,实质上也控制了下面队列pop不会删除新加入的坏橘子
                r, c = queue.pop(0)         # 取出队列开头的坏橘子坐标，这体现了队列，前面删后面加
                if r-1>=0 and grid[r-1][c] == 1:# 上邻有好橘子
                    grid[r-1][c] = 2        # 好橘子变坏
                    count -= 1              # 好橘子数-1
                    queue.append((r-1, c))
                if r+1<row and grid[r+1][c] == 1:# 下邻有好橘子
                    grid[r+1][c] = 2
                    count -= 1
                    queue.append((r+1, c))
                if c-1>=0 and grid[r][c-1] == 1:# 左邻有好橘子
                    grid[r][c-1] = 2
                    count -= 1
                    queue.append((r, c-1))
                if c+1<col and grid[r][c+1] == 1:# 右邻有好橘子
                    grid[r][c+1] = 2
                    count -= 1
                    queue.append((r, c+1))
        return -1 if count > 0 else round_count  # 有好橘子返回-1，否则返回腐烂次数


        # BFS的标准实现是用队列。
        # 队列实现BFS的方法相对固定，大致分三步：
        # 1、初始化队列；
        # 2最开始的坏橘子全部入队，具体是橘子的坐标和time
        # 3循环：当队列不为空时，先弹出队首元素，然后将这个元素能够腐烂的橘子全部入队。
        row,col,time = len(grid), len(grid[0]), 0
        queue = []
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)] # 上、下、左、右
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 2:
                    queue.append((r, c, time))
        
        while queue:
            r,c,time = queue.pop(0)
            for dr, dc in directions:
                if 0 <= r+dr < row and 0<= c+dc < col and grid[r+dr][c+dc] == 1: # 通过这种方法控制方向
                    grid[r+dr][c+dc] = 2
                    queue.append((r+dr, c+dc, time+1))
        for row in grid:
            if 1 in row:
                return -1
        return time
        



class Solution {
public:
    int orangesRotting(vector<vector<int>>& grid) {
		int row = grid.size();
		int col = grid[0].size();
		int time = 0;
		int fresh_oranges = 0;
		deque<pair<pair<int, int>, int>> bad_oranges;
        // deque （全名 double ended queue）是一种具有队列和栈一样的数据结构。
        // 在c++标准库中几乎和vector容器的接口完全相同，不同 ：deque 容器在头和尾都可已进行插入和移除，而vector只能在尾部。
        // pair是将2个数据组合成一组数据,主要的两个成员变量是first second
        vector<pair<int, int>> directions = {{0,-1},{0,1},{-1,0},{1,0}};
		for(int r=0; r<row; r++){
			for(int c=0; c<col; c++){
				if(grid[r][c] == 2){
					bad_oranges.push_back({{r, c}, time});
				}
				else if(grid[r][c]==1){
					fresh_oranges ++;
				}
			}
		}

		while(!bad_oranges.empty()){
			pair<pair<int, int>, int> current_bad_oranges = bad_oranges.front();
			bad_oranges.pop_front();
            time = current_bad_oranges.second;
			for(auto dir: directions){
				int row_index = current_bad_oranges.first.first + dir.first;
				int col_index = current_bad_oranges.first.second + dir.second;
				if (row_index >= 0 && row_index < row &&
					col_index >= 0 && col_index < col &&
					grid[row_index][col_index] == 1){
					grid[row_index][col_index] = 2;
					fresh_oranges --;
					bad_oranges.push_back({{row_index, col_index}, time+1});
				}
			}
		}
		if(fresh_oranges != 0)
			return -1;
		return time;
    }
};