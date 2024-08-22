class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        newNum = ""
        b1 = str(bin(num)[2:])
        for i in range(len(b1)):
            if b1[i] == "1":
                newNum += "0"
            else:
                newNum += "1"
        return int(newNum, 2)

# Test Cases
solution = Solution()

expected1 = 2
ans1 = solution.findComplement(5)
assert ans1 == expected1, f"Test case 1 failed: {ans1}"

expected2 = 0
ans2 = solution.findComplement(7)
assert ans2 == expected2, f"Test case 2 failed: {ans2}"

expected3 = 0
ans3 = solution.findComplement(1)
assert ans3 == expected3, f"Test case 3 failed: {ans3}"

expected4 = 5
ans4 = solution.findComplement(10)
assert ans4 == expected4, f"Test case 4 failed: {ans4}"

expected5 = 1
ans5 = solution.findComplement(0)
assert ans5 == expected5, f"Test case 5 failed: {ans5}"

print("All test cases passed!")
