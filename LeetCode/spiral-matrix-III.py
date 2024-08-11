class Solution(object):
    def spiralMatrixIII(self, rows, cols, rStart, cStart):
        """
        :type rows: int
        :type cols: int
        :type rStart: int
        :type cStart: int
        :rtype: List[List[int]]
        """
        i, j = rStart, cStart

        diri, dirj = 0, 1
        twice = 2
        res = []
        moves = 1
        nextmove = 2

        while len(res) < (rows * cols):
            if (-1 < i < rows) and (-1 < j < cols):
                res.append([i, j])
            i += diri
            j += dirj
            moves -= 1
            if moves == 0:
                diri, dirj = dirj, -diri
                twice -= 1
                if twice == 0:
                    twice = 2
                    moves = nextmove
                    nextmove += 1
                else:
                    moves = nextmove - 1
        return res