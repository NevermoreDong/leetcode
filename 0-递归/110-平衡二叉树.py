class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        # 自底向上
        if not root: return True
        def recursive(node):
            if not node:
                return 0
            left_depth = recursive(node.left) + 1 # 直到最后一层才退出，这就是递归关闭的顺序
            right_depth = recursive(node.right) + 1
            if abs(left_depth - right_depth) > 1:
                self.res = False

            return max(left_depth, right_depth)

        self.res = True
        recursive(root)
        return self.res