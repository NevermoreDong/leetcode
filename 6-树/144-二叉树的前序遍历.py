# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        # def dfs(node):
        #     if not node:
        #         return
        #     res.append(node.val)
        #     if node.left:
        #         dfs(node.left)
        #     if node.right:
        #         dfs(node.right)
        # res = []
        # dfs(root)
        # return res

        if not root: return []
        queue = [root]
        res = []
        while queue:
            node = queue.pop()
            res.append(node.val)
            if node.right:
                queue.append(node.right)
            if node.left:
                queue.append(node.left)

        return res