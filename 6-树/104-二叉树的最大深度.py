class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        # bfs
        # if not root: return 0
        # depth = 0
        # queue = [root]
        # while queue:
        #     depth += 1
        #     length = len(queue)
        #     for _ in range(length):
        #         cur_node = queue.pop(0)
        #         if cur_node.left: queue.append(cur_node.left)
        #         if cur_node.right: queue.append(cur_node.right)
        # return depth
        # dfs
        if not root: return 0
        self.max_depth = 0
        def dfs(node, depth):
            if not node:
                return 
            self.max_depth = max(self.max_depth, depth)
            dfs(node.left, depth+1)
            dfs(node.right, depth+1)
        dfs(root, 0)
        return self.max_depth+1