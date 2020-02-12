from collections import deque


class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        if len(board) == 0:
            return
        nrow = len(board)
        ncol = len(board[0])
        directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        visited = set()
        bounds = set()
        # adding all boundary positions into a set using 2 loops
        for i in [0, nrow - 1]:
            for j in range(ncol):
                bounds.add((i, j))
        for i in [0, ncol - 1]:
            for j in range(nrow):
                bounds.add((j, i))
        """
        Graph BFS starts here.
        from each bound we traverse and mark the 0's which will not be flipped as K's
        """

        for i, j in bounds:
            if board[i][j] == "O":
                queue = deque([])
                queue.append((i, j))
                while queue:
                    i, j = queue.popleft()
                    if (i, j) in visited:
                        continue
                    board[i][j] = "K"
                    visited.add((i, j))
                    for a, b in directions:
                        if not (i + a < 0 or i + a >= nrow - 1 or b + j < 0 or b + j >= ncol - 1):
                            if board[i + a][j + b] == "O":
                                queue.append((i + a, b + j))
        """
        Now loop through the whole matrix and flip K's to O's and O's to X's
        """
        for i in range(nrow):
            for j in range(ncol):
                if board[i][j] == "K":
                    board[i][j] = "O"
                elif board[i][j] == "O":
                    board[i][j] = "X"
        return board