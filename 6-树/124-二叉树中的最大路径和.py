class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = float('-inf')

        def dfs(root):
            if not root: return 0
            val = root.val
            sum_left = max(0, dfs(root.left))
            sum_right = max(0, dfs(root.right))
            
            node_sum = val + sum_left + sum_right
            self.res = max(self.res, node_sum)
            return max(sum_right,sum_left) + val
        
        dfs(root)
        return self.res