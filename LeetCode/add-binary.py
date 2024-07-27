class Solution(object):
    """
    Class representing a solution for adding binary numbers.
    """
    def addBinary(self, a, b):
        """
        Adds two binary numbers and returns the result as a binary string.

        :param a: The first binary number as a string.
        :param b: The second binary number as a string.
        :return: The sum of the two binary numbers as a binary string.
        """
        i, j = len(a) - 1, len(b) - 1
        carry = 0
        result = []
        
        while i >= 0 or j >= 0 or carry:
            # Get the current digits (0 if the index is out of bounds)
            digit_a = int(a[i]) if i >= 0 else 0
            digit_b = int(b[j]) if j >= 0 else 0
            
            # Calculate the sum and the new carry
            total = digit_a + digit_b + carry
            carry = total // 2
            result.append(str(total % 2))
            
            # Move the pointers
            i -= 1
            j -= 1
        
        # The result is currently in reverse order
        return ''.join(reversed(result))
