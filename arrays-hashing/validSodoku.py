import collections

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # create empty sets to store every unique value in each row, coloumn and 3 x 3 grid
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        # the key for the 3 x 3 sub grids will be a touple in the format: (row# // 3, col# // 3)
        # this integer division allows us to compute and track which subgrid a given value belongs to (0, 1, 2)
        subGrids = collections.defaultdict(set)
        # iterate through rows
        for r in range(9):
            #iterate through columns
            for c in range(9):
                # check if value is empty
                if (board[r][c] == '.'):
                    continue
                # check if value exists in each of our sets using our iterators as keys, and a computed touple for the subgrid set
                if (board[r][c] in rows[r] or
                    board[r][c] in cols[c] or
                    board[r][c] in subGrids[(r // 3, c // 3)]):
                    # if it exists the board is invalid and we return false
                    return False
                # if they dont exist then we add those values to the current set and reiterate
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                subGrids[(r // 3, c // 3)].add(board[r][c])
        # if our invalid condition doesnt get hit then return true
        return True