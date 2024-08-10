class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or numRows >= len(s):
            return s

        rows = [[] for row in range(numRows)]
        index = 0
        step = -1
        for char in s:
            rows[index].append(char)
            if index == 0:
                step = 1
            elif index == numRows - 1:
                step = -1
            index += step

        for i in range(numRows):
            rows[i] = ''.join(rows[i])
        print(rows)
        return ''.join(rows)
if __name__ == "__main__":
    solution = Solution()

    # Test Case 1
    s1 = "PAYPALISHIRING"
    numRows1 = 3
    expected1 = "PAHNAPLSIIGYIR"
    output1 = solution.convert(s1, numRows1)
    assert output1 == expected1, f"Test case 1 failed: {output1}"

    # Test Case 2
    s2 = "PAYPALISHIRING"
    numRows2 = 4
    expected2 = "PINALSIGYAHRPI"
    output2 = solution.convert(s2, numRows2)
    assert output2 == expected2, f"Test case 2 failed: {output2}"

    # Test Case 3
    s3 = "AB"
    numRows3 = 1
    expected3 = "AB"
    output3 = solution.convert(s3, numRows3)
    assert output3 == expected3, f"Test case 3 failed: {output3}"

    print("All test cases passed!")
