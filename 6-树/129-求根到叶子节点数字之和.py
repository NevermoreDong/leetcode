class Solution(object):
    def sumNumbers(self, root):
        # if root == None:
        #     return 0
        # def dfs(node, val):
        #     if not node:
        #         return
        #     val = 10*val + node.val
        #     if not node.left and not node.right:
        #         result.append(val)
        #         return
        #     if node.left:
        #         dfs(node.left, val)
        #     if node.right:
        #         dfs(node.right, val) 
        # val = 0
        # result = []
        # dfs(root, val)
        # return sum(result)

        if not root: return 0
        res = []
        queue = [(root, str(root.val))]
        while queue:
            node, path_cnt = queue.pop(0)
            if node.left:
                queue.append((node.left, path_cnt+str(node.left.val)))
            if node.right:
                queue.append((node.right, path_cnt+str(node.right.val)))
            if not node.left and not node.right:
                res.append(path_cnt)
        return sum(map(int, res))