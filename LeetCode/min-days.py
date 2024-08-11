class Solution(object):
    def minDays(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        counter = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    counter += 1
                    root = (i, j)
        if counter <= 1: 
            return counter
        
        vis, low, time, res = {root}, {}, {}, []

        def points(curr, parent):
            low[curr] = time[curr] = len(vis)
            children = 0
            i, j = curr

            for x, y, in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if (x, y) == parent:
                    continue
                if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y]:
                    if (x, y) not in vis:
                        vis.add((x, y))
                        points((x, y), curr)
                        low[curr] = min(low[curr], low[(x, y)])
                        children += 1
                        if low[(x, y)] >= time[(curr)] and parent != (-1, -1):
                            res.append([i, j])
                    else:
                        low[curr] = min(low[curr], time[(x, y)])

                if parent == (-1, -1) and children > 1:
                    res.append([x, y])
        points(root, (-1, -1))

        if len(vis) != counter:
            return 0
        elif res:
            return 1
        else:
            return 2


# Example 1:
# Input: grid = [[0,1,1,0],[0,1,1,0],[0,0,0,0]]
# Output: 2
# Explanation: The island has two connected cells.
# Example 2:
# Input: grid = [[1,1]]
# Output: 2
# Explanation: The island has just one cell.
# Example 3:
# Input: grid = [[1,0,1,0]]
# Output: 0
# Explanation: There is no way to have a single island.
# Constraints:
# 1 <= grid.length, grid[i].length <= 50


# Test case 1: Basic test case with a single connected island
grid1 = [[0,1,1,0],[0,1,1,0],[0,0,0,0]]
expected_output1 = 2
assert Solution().minDays(grid1) == expected_output1

# Test case 2: Basic test case with a single island
grid2 = [[1,1]]
expected_output2 = 2
assert Solution().minDays(grid2) == expected_output2

# Test case 3: Test case with no connected islands
grid3 = [[1,0,1,0]]
expected_output3 = 0
assert Solution().minDays(grid3) == expected_output3

print("All test cases passed!")