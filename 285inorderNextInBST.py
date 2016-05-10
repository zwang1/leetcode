

class Solution(object):
    def inorderSuccessor(self, root, node):
        if not node:
            return None
        if node.right:
            return self.minright(node.right)
        else:
            return self.lastbig(root, None, node.val)

    def minright(self, root):
        min = root
        while root.left:
            root = root.left
            min = root
        return min

    def lastbig(self, root, last, n):
        while root.val != n:
            if root.val > n:
                last = root
                root = root.left
                
            else:
                root = root.right
        return last
