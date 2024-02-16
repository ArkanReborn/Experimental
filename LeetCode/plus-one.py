class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digits = [str(i) for i in digits]
        digits = (''.join(digits))
        digits = int(digits)
        digits += 1
        digits = [int(i) for i in str(digits)]
        return list(digits)
    # Run Time 14ms beats 75% of Python users
    # Memory 11.50 MB beats 90.10% of Python users

nums = Solution()
print(nums.plusOne((1,4,2))) # Outputs [1, 4, 3]
print(nums.plusOne((9,9,9,9))) # Outputs [1, 0, 0, 0, 0]