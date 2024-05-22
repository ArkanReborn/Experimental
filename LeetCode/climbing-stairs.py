class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 1:
            return 1

        dp = [0] * (n + 1)
        dp[0] = dp[1] = 1

        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
            # print(f"{dp[i]} stairs climbed")

        return dp[n]
    # 7 ms beats 95.2% of python submissions
    # 11.68 mbs beats 67.53% of python submissions


stairs = Solution()
print(stairs.climbStairs(2))  # 2 Stairs climbed
print(stairs.climbStairs(6))  # 3 Stairs climbed
