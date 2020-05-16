class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        # if not root: return []
        # res = []
        # queue = [root]
        # flag = -1       
        # while queue:
        #     layer_val = []
        #     next_layer = []
        #     for node in queue:
        #         layer_val.append(node.val)
        #         if node.left: next_layer.append(node.left)
        #         if node.right: next_layer.append(node.right)
        #     flag *= -1
        #     if flag>0 :
        #         res.append(layer_val)
        #     else:
        #         res.append(layer_val[::-1])
        #     queue = next_layer
        # return res

        if not root:return []
        res = []
        def dfs(node, layer_cnt):
            if len(res) == layer_cnt:
                res.append([])
            if layer_cnt % 2 == 0:
                res[layer_cnt].append(node.val)
            else:
                res[layer_cnt].insert(0, node.val)
            if node.left: dfs(node.left, layer_cnt+1)
            if node.right: dfs(node.right, layer_cnt+1)
        dfs(root, 0)
        return res