class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        queue = [root]
        res = []
        while queue:
            cur_queue = []
            cur_val = []
            for node in queue:
                cur_val.append(node.val)
                if node.left: cur_queue.append(node.left)
                if node.right: cur_queue.append(node.right)
            res.insert(0, cur_val)
            queue = cur_queue
        return res