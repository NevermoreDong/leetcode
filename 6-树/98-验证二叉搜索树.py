class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        Tree = []
        def mid(node):
            if not node:
                return 
            mid(node.left)
            Tree.append(node.val)
            mid(node.right)
        mid(root)
        return Tree == sorted(Tree) and len(Tree) == len(set(Tree))
        # 因为二叉搜索树中序遍历是递增的,所以我们可以中序遍历判断前一数是否小于后一个数.