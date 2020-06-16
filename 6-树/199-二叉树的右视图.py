# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root: return []
        queue = [root]
        res = []
        while queue:
            res.append(queue[-1].val)
            next_layer = []
            for _ in range(len(queue)):
                node = queue.pop(0)
                if node.left: next_layer.append(node.left)
                if node.right: next_layer.append(node.right)
            queue = next_layer
        return res