'''
解题思路 :题目给定的是一个无向简单图，要求找出最高树的节点，
首先通过分析可以知道，最后的根节点只可能为1个或者2个。
要求最小高度的根节点，我们反过来想，怎样才能求得最小高度呢，很容易想到从叶子节点开始往根找，
于是就是采用分层剥削的方法，每次去除一层叶子节点，这样保证最后的节点就是我们所要的。
'''

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        degree = [0]*n #节点的度
        result = set([x for x in range(n)])  #待选节点，一开始时全部节点，然后将叶子节点逐层删掉
        if(not n > 2):
            return list(result)
        graph = [[] for x in range(n)]  #构建地图和节点的度，不能[[]]*n，因为里面的[]内存地址一样
        for node1,node2 in edges:
            graph[node1].append(node2)
            graph[node2].append(node1)
            degree[node1] += 1
            degree[node2] += 1
        queue = []
        for cur in range(n): #初始入队，将叶子节点（节点度为1的节点）入队
            if (degree[cur] == 1):
                queue.append(cur)
                result.remove(cur) #入队说明该节点不可能成为根节点了。
        while len(result) > 2:
            length = len(queue) #获取队列的个数，主要是为了一层一层的遍历
            for _ in range(length):
                cur = queue.pop(0)
                for next in graph[cur]:
                    degree[next] -= 1
                    if(degree[next] == 1):
                        queue.append(next)
                        result.remove(next)
        return list(result)


## 求树的高度
tree = [[0,1],[0,2],[1,3],[1,4],[2,7],[2,6],[4,5]]
def deep(tree):
    count = set()
    for l in tree:
        count.add(l[0])
        count.add(l[1])
    nums = len(list(count))
    graph = [[] for i in range(nums)]
    for start, end in tree:
        graph[start].append(end)
    deepth = 0
    queue = []
    queue.append(0)
    while queue:
        length = len(queue)
        deepth += 1
        for _ in range(length):
            cur_node = queue.pop(0)
            for next_node in graph[cur_node]:
                queue.append(next_node)
    return deepth

print(deep(tree))



