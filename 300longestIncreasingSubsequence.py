__author__ = 'zhengyiwang'


class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        # for store the smallest number at length i
        '''
        [10,26,77] means last smallest number of a subsquence of length 1 is 10,
                        last smallest number of a subsquence of length 2  is 26
                        last smallest number of a subsquence of length 3 is 77
        '''
        longest = [nums[0]]

        def findposition(n):
            start, end = 0, len(longest) - 1
            while start <= end:
                mid = (start + end) / 2
                if longest[mid] > n:
                    end = mid - 1
                elif longest[mid] < n:
                    start = mid + 1
                else:
                    return
            if start == len(longest):
                longest.append(n)
            else:
                longest[start] = n


        for n in nums:
            findposition(n)
        return len(longest)

if __name__ == "__main__":
    s = Solution()
    a = [3,5,6,2,5,4,19,5,6,7,12]
    s.lengthOfLIS(a)

