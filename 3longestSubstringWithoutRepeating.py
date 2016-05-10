__author__ = 'zhengyiwang'

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        dp = [1 for i in range(len(s))]
        position = {s[0]: 0}
        m = 1
        for i in range(1,len(s)):
            c = s[i]
            if c not in position:
                dp[i] = dp[i - 1] + 1
            else:
                dp[i] = min(i - position[c], dp[i - 1]+ 1)
            position[c] = i
            m = max(m,dp[i])

        return m


if __name__ == "__main__":
    s = Solution()
    print s.lengthOfLongestSubstring("anna")

