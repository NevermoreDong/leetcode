class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root: return 0
        min_depth = []
        def dfs(node, depth):
            if not node:
                return
            if not node.left and not node.right:
                min_depth.append(depth)
            if node.left: dfs(node.left, depth+1)
            if node.right: dfs(node.right, depth+1)
        dfs(root, 1)
        return min(min_depth)