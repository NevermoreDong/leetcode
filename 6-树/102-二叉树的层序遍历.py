class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        # res = []
        # queue = [root]
        # while queue:
        #     length = len(queue)
        #     layer_val = []
        #     for _ in range(length):
        #         node = queue.pop(0)
        #         if node:
        #             queue.append(node.left)
        #             queue.append(node.right)
        #             layer_val.append(node.val)
        #     if len(layer_val) != 0:
        #         res.append(layer_val)
        # return res
        ## dfs ##
        if not root: return []
        def dfs(node, layer_cnt):
            if len(res) == layer_cnt:
                res.append([])
            res[layer_cnt].append(node.val)
            if node.left:
                dfs(node.left, layer_cnt+1)
            if node.right:
                dfs(node.right, layer_cnt+1)
        res = []
        dfs(root, 0)
        return res