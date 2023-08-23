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