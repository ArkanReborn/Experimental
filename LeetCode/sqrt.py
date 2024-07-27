class Solution(object):
    """
    Class representing a solution for finding the square root of a number.
    """

    def mySqrt(self, x):
        """
        Finds the square root of a given number.

        Args:
            x (int): The number for which the square root needs to be found.

        Returns:
            int: The square root of the given number.
        """
        if x == 0 or x == 1:
            return x
        
        left, right = 0, x
        while left <= right:
            mid = (left + right) // 2
            mid_squared = mid * mid

            if mid_squared == x:
                return mid
            elif mid_squared < x:
                left = mid + 1
            else:
                right = mid - 1
        return right
