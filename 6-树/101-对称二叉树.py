class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def isSame(q,p):
            if q and p and q.val == p.val:
                return isSame(q.left, p.right) and isSame(q.right, p.left)
            if not q and not p:
                return True
            return False
        if root is None:
            return True
        return isSame(root.left, root.right)


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        queue = [root]
        while queue:
            layer = []
            length = len(queue)
            for _ in range(length):
                cur_node = queue.pop(0)
                if not cur_node:
                    layer.append(None)
                    continue
                queue.append(cur_node.left)
                queue.append(cur_node.right)
                layer.append(cur_node.val)
            if layer != layer[::-1]:
                return False
        return True