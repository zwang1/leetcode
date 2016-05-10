__author__ = 'zhengyiwang'
class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """

        result = [[0] * len(matrix[0]) for i in range(len(matrix))]
        for row in range(len(result)):
            for col in range(len(result[0])) :

                self.dfs(matrix,col,row,result)
        longest = 1
        for row in result:
            longest = max(max(row), longest)
        return longest

    def dfs(self, matrix, x,y,result):
        if result[y][x] >= 1:
            return
        update = 1
        neibor = self.smallneibor(x,y,matrix)
        for nextx,nexty in neibor:
            self.dfs(matrix, nextx, nexty, result)
            update = max(update, result[nexty][nextx] + 1)
        result[y][x] = update
    def smallneibor(self,x,y,matrix):
        smalls = []
        for nextx, nexty in [[x-1,y],[x+1,y],[x, y-1],[x,y + 1]]:
                if 0 <= nextx<len(matrix[0]) and 0 <= nexty< len(matrix):
                    if matrix[nexty][nextx] < matrix[y][x]:
                        smalls.append([nextx,nexty])
        return smalls

if __name__ == "__main__":
    s = Solution()
    nums = [[3,4,5],[3,2,6],[2,2,1]]

    print s.longestIncreasingPath(nums)
