__author__ = 'zhengyiwang'
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <2:
            return nums[0]

        pos = [ nums[0]]* len(nums)
        neg = [0] * len(nums)
        if nums[0] < 0:
            pos, neg = neg, pos
        for i in range(1, len(nums)):
            c = nums[i]
            if c < 0:
                neg[i] = c if pos[i - 1] == 0 else pos[i - 1] * c
                pos[i] = c * neg[i - 1]

            else:
                pos[i] = c if pos[i - 1] == 0 else pos[i- 1] * c
                neg[i] = c * neg[i - 1]
        max = nums[1]
        for n in pos:
            if max < n:
                max = n
        return max
    def maxproduct2(self,nums):
        pos, neg = 1, 1
        max = nums[0]
        for n in nums:
            pos, neg = max(n, n*pos, n*neg), min(n,n*pos,n*neg)
            if max < pos:
                max = pos
        return max