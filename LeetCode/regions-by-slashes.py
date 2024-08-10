class Solution(object):
    def regionsBySlashes(self, grid):
        """
        :type grid: List[str]
        :rtype: int
        """
        roots = {}
        def find(x):
            if x not in roots:
                roots[x] = x
            while (x != roots[x]):
                x = roots[x]
            return x
        def union(x, y):
            roots[find(x)] = find(y)
        length = len(grid)
        for i in range(length):
            for j in range(length):
                # Check if character is "/"
                if grid[i][j] == "/":
                    union((i, j, "N"), (i, j, "W"))
                    union((i, j, "S"), (i, j, "E"))
                # Check if the character is "\"
                elif grid[i][j] == "\\":
                    union((i, j, "N"), (i, j, "E"))
                    union((i, j, "S"), (i, j, "W"))
                # Check if the character is " "
                elif grid[i][j] == " ":
                    union((i, j, "N"), (i, j, "E"))
                    union((i, j, "S"), (i, j, "W"))
                    union((i, j, "N"), (i, j, "W"))
                # Check horizontally adjacent squares, 
                # union the E from the left with W from the right square
                if j > 0:
                    union((i, j-1, "E"), (i, j, "W"))
                # Check vertically adjacent squares,
                # Union the S from the top square with N from the bottom square
                if i > 0:
                    union((i - 1, j, "S"), (i, j, "N"))
        return len(set(map(find, roots)))
    
