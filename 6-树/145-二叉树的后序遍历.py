# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        # def dfs(node):
        #     if not node:
        #         return
        #     dfs(node.left)
        #     dfs(node.right)
        #     res.append(node.val)
        # res = []
        # dfs(root)
        # return res

        if not root: return []
        stack = [root]
        res = []
        while stack:
            node = stack.pop()
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
            res.append(node.val)
        return res[::-1]