"""

Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be 
validated according to the following rules:

Each row must contain the digits 1-9 without repetition.

Each column must contain the digits 1-9 without repetition.

Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.

Example 1:


Input: board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true


Example 2:

Input: board = 
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: false

Explanation: Same as Example 1, except with the 5 in the top left corner
 being modified to 8. Since there are two 8's in
  the top left 3x3 sub-box, it is invalid.


Constraints:

board.length == 9
board[i].length == 9
board[i][j] is a digit 1-9 or '.'.


Takeaway:

compartmentalize of the code is the single greatest thing you can learn.

zip() can be usec to combine multiple sequences iwth respect to their index.\

zip() function is used to combine two or more lists (or any other iterables) into
 a single iterable, where elements from corresponding positions are paired together.

unzipping values:

To unzip something zipped, use * on it just like tuple unpacking
    namz, roll_noz, marksz = zip(*mapped)


"""

class Solution:
    def isValidSudoku_first(self, board) -> bool:
        
        # board is made of strings.
        # none means .

        # check left to right
        for elem in board:
            # if there is a duplicate in the row, return False
            _counter = []
            for cell in elem:
                if cell == ".":
                    pass
                _counter.append(cell)
                if len(_counter) != len(set(_counter)):
                    return False            
            del _counter


        column_checker = [i for i in range(9)]
        # check top to bottom
        for elem in board:
            # if there is a duplicate in the column, return False
            cols = [elem[i] for i in range(9)]

            pass

        # check 3 by 3s
        for elem in board:
            pass

        return True
    
    # compartmentelize the solution
    def isValidSudoku(self, board):

        def is_valid(value):
            # all the values except Nones, which are "." s.
            res = [i for i in value if i != '.']
            # is there a duplicate?
            return len(res) == len(set(res))

        def is_valid_row(board):
            for row in board:
                if not is_valid(row):
                    return False
            return True

        def is_valid_column(board):
            for col in zip(*board): 
                if not is_valid(col):
                    return False
            return True

        def is_valid_square(board):
            for i in (0,3,6):
                for j in (0,3,6):
                    square = [board[x][y] for x in range(i,i+3) 
                                            for y in range(j,j+3)]
                    if not is_valid(square):
                        return False
            return True

        # we check 3 things.
        return is_valid_row(board) and is_valid_column(board) and is_valid_square(board)


if __name__ == "__main__":
    sol = Solution()

    board_1 = [["5","3",".",".","7",".",".",".","."],
               ["6",".",".","1","9","5",".",".","."],
               [".","9","8",".",".",".",".","6","."],
               ["8",".",".",".","6",".",".",".","3"],
               ["4",".",".","8",".","3",".",".","1"],
               ["7",".",".",".","2",".",".",".","6"],
               [".","6",".",".",".",".","2","8","."],
               [".",".",".","4","1","9",".",".","5"],
               [".",".",".",".","8",".",".","7","9"]]

    board_2 = [["8","3",".",".","7",".",".",".","."],
               ["6",".",".","1","9","5",".",".","."],
               [".","9","8",".",".",".",".","6","."],
               ["8",".",".",".","6",".",".",".","3"],
               ["4",".",".","8",".","3",".",".","1"],
               ["7",".",".",".","2",".",".",".","6"],
               [".","6",".",".",".",".","2","8","."],
               [".",".",".","4","1","9",".",".","5"],
               [".",".",".",".","8",".",".","7","9"]]

    print(sol.isValidSudoku(board_1))
    print(sol.isValidSudoku(board_2))

