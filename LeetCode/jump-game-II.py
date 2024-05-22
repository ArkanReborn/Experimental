class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numLen, curr, nxt, ans, i = len(nums) -1, -1, 0, 0, 0
        while nxt < numLen:
            if i > curr:
                ans += 1
                curr = nxt
            nxt = max(nxt, nums[i] + i)
            i += 1
        return ans

# Test case 1: Basic test case with a single jump
nums = [2, 3, 1, 1, 4]
expected_output = 2
assert Solution().jump(nums) == expected_output

# Test case 2: Basic test case with multiple jumps
nums = [3, 2, 1, 0, 4]
expected_output = 2
assert Solution().jump(nums) == expected_output

# Test case 3: Test case with no jumps required
nums = [0]
expected_output = 0
assert Solution().jump(nums) == expected_output

# Test case 4: Test case with large input
nums = [1] * 10000
expected_output = 9999
assert Solution().jump(nums) == expected_output

# Test case 5: Test case with negative numbers
nums = [-1, -2, -3, -4, -5]
expected_output = 4
assert Solution().jump(nums) == expected_output

print("All test cases passed!")