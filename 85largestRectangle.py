__author__ = 'zhengyiwang'
class Su(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """

        if not matrix:
            return 0

        n = len(matrix)
        m = len(matrix[0])
        height = [int(x) for x in matrix[0]]
        maxarea  = self.bst(height, 0 , m -1)
        for j in range(1, n):
            for i in range(0, m ):
                if matrix[j ][i] == "0":
                    height[i] = 0
                else:
                    height[i] = height[i] + 1
            maxarea = max(maxarea, self.bst(height, 0 , m -1))


        return maxarea

    def bst(self, nums, start, end):
        if start > end:
            return 0
        short = start
        increase = True
        for i in range(start + 1, end + 1):
            if increase:
                if nums[i] < nums[i - 1]:
                    increase = False
            if nums[short] > nums[i]:
                short = i
        if increase:
            maxarea = 0
            for i in range(start, end + 1):
                maxarea = max(maxarea, nums[i] * (end - i + 1))
            return maxarea
        left = self.bst(nums,start, short - 1)
        right = self.bst(nums, short + 1, end)
        return max(left, right, nums[short] * (end - start + 1))

s = Su()

print s.maximalRectangle(["10","10"])