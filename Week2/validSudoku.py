class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        map_row = [set() for _ in range(9)]
        map_col = [set() for _ in range(9)]
        map_cell = [[set() for _ in range(3)] for _ in range(3)]

        for i in range(9):
            for j in range(9):
                cur = board[i][j]
                if cur == ".":
                    continue
                # row check
                if cur in map_row[i]:
                    return False
                else:
                    map_row[i].add(cur)
                # column check
                if cur in map_col[j]:
                    return False
                else:
                    map_col[j].add(cur)
                # cell check
                if cur in map_cell[i // 3][j // 3]:
                    return False
                else:
                    map_cell[i // 3][j // 3].add(cur)
        return True