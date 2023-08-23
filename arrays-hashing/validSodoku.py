class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # create dict variable to hold columns
        dict = {0:[], 1:[], 2:[], 3:[], 4:[], 5:[], 6:[], 7:[], 8:[]}
        # check if row contains duplicate numbers
        for i in range(0, 9):
            # remove periods from list
            myFilter = filter(lambda x: (x.isnumeric()), board[i])
            filtered = set(list(myFilter))
            # remove duplicates using set constructor
            mySet = set(filtered)
            # check if length of filtered and set are not equal
            if len(filtered) != len(mySet):
                return False


            # check if column contains duplicate numbers
            for j in range(0, 9):
                # append each value to dict to get arrays of column values
                dict[j].append(board[i][j])

            # repeat filtering logic
            colFilter = filter(lambda x: (x.isnumeric()), dict[j])
            colFiltered = list(colFilter)
            colSet = set(colFiltered)

            # check if length of filtered and set are not equal
            if len(colFiltered) != len(colSet):
                return False  
        # check if 3x3 contains duplicates
         