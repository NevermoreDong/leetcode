class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        # 简单来说就是求图的两点最短路径，每个单词是一个点，只有相差一个字符的点之间才有路径，路径权值全部为1
        wordList = set(wordList)
        queue = [(beginWord, 1)] # 如果想早得到深度，得写一起

        if endWord not in wordList : return 0

        while queue:

            node, depth = queue.pop(0)
            if node == endWord:
                return depth

            for i in range(len(node)):
                for chr_num in range(97, 123):
                    word = node[:i] + chr(chr_num) + node[i+1:]
                    if word in wordList:
                        queue.append((word, depth+1))
                        wordList.remove(word)
        return 0
