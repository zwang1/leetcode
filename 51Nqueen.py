__author__ = 'zhengyiwang'
class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        result = []
        self.dfs(0, n, set([]), set([]), set([]), [], result)
        return result

    #for each row put a new queue
    #check each position in this row for:
    #any existing queen in this col or /(i+j) or \(i-j) directions of line

    def dfs(self, index, n, col, sum, diff, solution, result):
        if index == n:
            result.append(solution)
            return
        for p in range(n):
            if p not in col and p - index not in diff and p + index not in sum:
                col.add(p)
                sum.add(p + index)
                diff.add(p - index)
                line = "." * p + "Q" + "." * (n - p - 1)
                self.dfs(index + 1, n, col, sum, diff, solution + [line], result)
                col.remove(p)
                sum.remove(p + index)
                diff.remove(p - index)

