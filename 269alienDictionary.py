__author__ = 'zhengyiwang'
class TrieNode():
    def __init__(self, c):
        self.val = c
        self.child = None
class TrieTree():
    def __init__(self):
        self.root = TrieNode('0')

    def insert(self, w, edges):
        self.root.child = self.__insert(self.root.child, w, 0, edges)

    def __insert(self, root, w, i, edges):
        if i == len(w):
            return root
        if root is None:
            root = TrieNode(w[i])
        elif root.val != w[i]:
            #update the root val and form an edge from pre to new
            if root.val not in edges:
                edges[root.val] = [w[i]]
            else:
                edges[root.val].append(w[i])

            root = TrieNode(w[i])

        root.child= self.__insert(root.child, w, i + 1, edges)
        return root



class Solution(object):
    def sort(self, words):
        edges = {}
        tree = TrieTree()
        marked = {}
        for w in words:
            tree.insert(w, edges)
            for c in w:
                marked[c] = False

        return self.topsort(edges,marked)

    def topsort(self, edges , marked):
        result = []
        for c in marked:
            if not self.dfs([], edges, marked, c, result):
                return ""
        return "".join(result[::-1])
    def dfs(self, path, edges, marked, c, result):
        if marked[c]:
            return True
        if c in path:
            return False
        noloop = True
        if c in edges:
            for outgoing in edges[c]:
                if not marked[outgoing]:
                    noloop &= self.dfs(path+[c], edges, marked, outgoing, result)
        if noloop:
            marked[c] = True
            result.append(c)
            return True
        else:
            return False
if __name__ == "__main__":
    s =Solution()
    words = ["za","zb","ca","cb"]
    a = s.sort(words)
    print a


