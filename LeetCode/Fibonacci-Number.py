class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            prev1 = 0
            prev2 = 1
            fib = 0
            for i in range(n - 1):
                fib = prev1 + prev2
                prev1 = prev2
                prev2 = fib
            return fib

        # 15 ms beats 68.62% of python submissions
        # 11.77 mbs beats 34.11% of python submissions


fib = Solution()
print(fib.fib(2))  # 1
print(fib.fib(3))  # 2
print(fib.fib(4))  # 3
